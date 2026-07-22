import discord

# DM ALERT EMBED
def create_dm_embed(author, message, channel, guild):
    embed = discord.Embed(
        title="👻 Ghost Ping Detected!",
        description="Someone mentioned you and deleted their message.",
        color=discord.Color.red()
    )

    embed.add_field(
        name="👤 Author",
        value=author.mention,
        inline=False
    )

    embed.add_field(
        name="🏠 Server",
        value=guild.name,
        inline=True
    )

    embed.add_field(
        name="📍 Channel",
        value=channel.mention,
        inline=True
    )

    embed.add_field(
        name="💬 Deleted Message",
        value=message if message else "*No text*",
        inline=False
    )

    embed.set_footer(
        text="GhostAlert • Never miss a ghost ping"
    )

    return embed

# LOG MESSAGE EMBED
def create_log_embed(author, victims, message, channel):
    embed = discord.Embed(
        title="🚨 Ghost Ping Logged",
        color=discord.Color.orange()
    )

    embed.add_field(
        name="👤 Author",
        value=author.mention,
        inline=False
    )

    victim_text = "\n".join(user.mention for user in victims)

    embed.add_field(
        name="🎯 Victims",
        value=victim_text,
        inline=False
    )

    embed.add_field(
        name="📍 Channel",
        value=channel.mention,
        inline=False
    )

    embed.add_field(
        name="💬 Deleted Message",
        value=message if message else "*No text*",
        inline=False
    )

    embed.set_footer(
        text="GhostAlert • Catch Ghost Pingers In 4K"
    )

    return embed
    
# STAFF DM ALERT EMBED  
def create_staff_dm_embed(author, message, channel, guild):
    embed = discord.Embed(
        title="🚨 GhostAlert Staff Notification",
        description="A ghost ping involving a role or global mention was detected.",
        color=discord.Color.gold()
    )

    embed.add_field(
        name="👤 Author",
        value=author.mention,
        inline=False
    )

    embed.add_field(
        name="🏠 Server",
        value=guild.name,
        inline=True
    )

    embed.add_field(
        name="📍 Channel",
        value=channel.mention,
        inline=True
    )

    embed.add_field(
        name="💬 Deleted Message",
        value=message if message else "*No text*",
        inline=False
    )

    embed.set_footer(
        text="GhostAlert • Staff Alert"
    )

    return embed