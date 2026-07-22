import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from database import setup_database
from commands import setup_commands
from database import (
    is_dm_enabled,
    get_log_channel,
    get_alert_recipients
)

from embeds import (
    create_dm_embed,
    create_log_embed,
    create_staff_dm_embed
)

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():

    await setup_database()

    synced = await bot.tree.sync()

    print(f"Synced {len(synced)} commands.")

    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    if message.author.bot:
        return

    user_ping = bool(message.mentions)

    staff_ping = (
        "<@&" in message.content
        or "@everyone" in message.content
        or "@here" in message.content
    )

    if not (user_ping or staff_ping):
        return


    # Send DMs to all victims
    for victim in message.mentions:

        if await is_dm_enabled(victim.id):

            embed = create_dm_embed(
                author=message.author,
                message=message.content,
                channel=message.channel,
                guild=message.guild
            )

            try:
                await victim.send(embed=embed)

            except discord.Forbidden:
                print(f"Couldn't DM {victim}")


    # Send staff DM alerts for role/everyone/here mentions
    if staff_ping:

        recipient_ids = await get_alert_recipients(message.guild.id)
        display_message = message.content

        for role in message.role_mentions:
            display_message = display_message.replace(
                role.mention,
                f"@{role.name}"
            )        
        
        staff_embed = create_staff_dm_embed(
            author=message.author,
            message=display_message,
            channel=message.channel,
            guild=message.guild
        )

        for user_id in recipient_ids:

            user = bot.get_user(user_id)

            if user is None:
                try:
                    user = await bot.fetch_user(user_id)
                except discord.NotFound:
                    continue

            try:
                await user.send(embed=staff_embed)
            except discord.Forbidden:
                pass


    # Send ONE log message
    log_channel_id = await get_log_channel(message.guild.id)

    if log_channel_id:

        log_channel = message.guild.get_channel(log_channel_id)

        if log_channel:

            embed = create_log_embed(
                author=message.author,
                victims=message.mentions,
                message=message.content,
                channel=message.channel
            )

            await log_channel.send(embed=embed)


setup_commands(bot.tree)
bot.run(TOKEN)