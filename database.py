import aiosqlite

DATABASE = "data.db"

# DATABASE SETUP
async def setup_database():
    async with aiosqlite.connect(DATABASE) as db:

        # User preferences
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            dm_enabled INTEGER DEFAULT 1
        )
        """)

        # Guild settings
        await db.execute("""
        CREATE TABLE IF NOT EXISTS guilds(
            guild_id INTEGER PRIMARY KEY,
            log_channel_id INTEGER
        )
        """)

        # Alert recipients
        await db.execute("""
        CREATE TABLE IF NOT EXISTS alert_recipients(
            guild_id INTEGER,
            user_id INTEGER,
            PRIMARY KEY(guild_id, user_id)
        )
        """)

        await db.commit()
        
"""
=========
FUNCTIONS
=========
"""

# ENABME DIRECT MESSAGE ALERTS        
async def enable_dm(user_id):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute("""
        INSERT OR REPLACE INTO users(user_id, dm_enabled)
        VALUES(?, 1)
        """, (user_id,))
        await db.commit()

# DISABLE DIRECT MESSAGE ALERTS        
async def disable_dm(user_id):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute("""
        INSERT OR REPLACE INTO users(user_id, dm_enabled)
        VALUES(?, 0)
        """, (user_id,))
        await db.commit()
        
# CHECK IF DM ALERT IS ENABLED        
async def is_dm_enabled(user_id):

    async with aiosqlite.connect(DATABASE) as db:

        cursor = await db.execute("""
        SELECT dm_enabled
        FROM users
        WHERE user_id=?
        """, (user_id,))

        row = await cursor.fetchone()

        if row is None:
            return True

        return bool(row[0])
        
# SELECTING LOG CHANNEL       
async def set_log_channel(guild_id, channel_id):

    async with aiosqlite.connect(DATABASE) as db:

        await db.execute("""
        INSERT OR REPLACE INTO guilds(guild_id, log_channel_id)
        VALUES(?, ?)
        """, (guild_id, channel_id))

        await db.commit()
        
        
# GET LOG CHANNEL        
async def get_log_channel(guild_id):

    async with aiosqlite.connect(DATABASE) as db:

        cursor = await db.execute("""
        SELECT log_channel_id
        FROM guilds
        WHERE guild_id=?
        """, (guild_id,))

        row = await cursor.fetchone()

        if row:
            return row[0]

        return None
        
        
# ALERT RECIPIENTS
async def add_alert_recipient(guild_id, user_id):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute("""
        INSERT OR IGNORE INTO alert_recipients(guild_id, user_id)
        VALUES(?, ?)
        """, (guild_id, user_id))

        await db.commit()
        
# REMOVE THEM
async def remove_alert_recipient(guild_id, user_id):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute("""
        DELETE FROM alert_recipients
        WHERE guild_id=? AND user_id=?
        """, (guild_id, user_id))

        await db.commit()
        
# GET RECIPIENTS
async def get_alert_recipients(guild_id):

    async with aiosqlite.connect(DATABASE) as db:

        cursor = await db.execute("""
        SELECT user_id
        FROM alert_recipients
        WHERE guild_id=?
        """, (guild_id,))

        rows = await cursor.fetchall()

        return [row[0] for row in rows]