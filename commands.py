import discord
from discord import app_commands

from database import (
    enable_dm,
    disable_dm,
    set_log_channel,
    add_alert_recipient,
    remove_alert_recipient,
    get_alert_recipients
)


def setup_commands(tree):

    # ENABLE DM ALERT COMMAND
    @app_commands.command(
        name="enable-dm-alert",
        description="Enable Ghost Ping DM alerts."
    )
    async def enable(interaction: discord.Interaction):

        await enable_dm(interaction.user.id)

        await interaction.response.send_message(
            "✅ Ghost Ping DM alerts have been enabled.",
            ephemeral=True
        )

    tree.add_command(enable)

    # DISABLE DM ALERT COMMAND
    @app_commands.command(
        name="disable-dm-alert",
        description="Disable Ghost Ping DM alerts."
    )
    async def disable(interaction: discord.Interaction):

        await disable_dm(interaction.user.id)

        await interaction.response.send_message(
            "✅ Ghost Ping DM alerts have been disabled.",
            ephemeral=True
        )

    tree.add_command(disable)

    # SET LOG CHANNEL COMMAND
    @app_commands.command(
        name="set-log-channel",
        description="Choose where ghost ping logs are sent."
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def log_channel(
        interaction: discord.Interaction,
        channel: discord.TextChannel
    ):

        await set_log_channel(
            interaction.guild.id,
            channel.id
        )

        await interaction.response.send_message(
            f"✅ Log channel set to {channel.mention}",
            ephemeral=True
        )

    tree.add_command(log_channel)

    # ADD DM LOG RECIPIENT
    @app_commands.command(
        name="add-dm-log-recipient",
        description="Adds a user to receive GhostAlert DM logs."
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def add_dm_log_recipient(
        interaction: discord.Interaction,
        user: discord.Member
    ):

        await add_alert_recipient(
            interaction.guild.id,
            user.id
        )

        await interaction.response.send_message(
            f"✅ {user.mention} will now receive GhostAlert DM logs.",
            ephemeral=True
        )

    tree.add_command(add_dm_log_recipient)

    # REMOVE DM LOG RECIPIENT
    @app_commands.command(
        name="remove-dm-log-recipient",
        description="Removes a user from GhostAlert DM logs."
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def remove_dm_log_recipient(
        interaction: discord.Interaction,
        user: discord.Member
    ):

        await remove_alert_recipient(
            interaction.guild.id,
            user.id
        )

        await interaction.response.send_message(
            f"✅ {user.mention} removed from GhostAlert DM logs.",
            ephemeral=True
        )

    tree.add_command(remove_dm_log_recipient)

    # LIST DM LOG RECIPIENTS
    @app_commands.command(
        name="list-dm-log-recipients",
        description="Lists all GhostAlert DM log recipients."
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def list_dm_log_recipients(
        interaction: discord.Interaction
    ):

        ids = await get_alert_recipients(interaction.guild.id)

        if not ids:
            await interaction.response.send_message(
                "❌ No DM log recipients have been configured.",
                ephemeral=True
            )
            return

        description = ""

        for uid in ids:
            member = interaction.guild.get_member(uid)

            if member:
                description += f"• {member.mention}\n"
            else:
                description += f"• Unknown User (`{uid}`)\n"

        embed = discord.Embed(
            title="📬 GhostAlert DM Log Recipients",
            description=description,
            color=discord.Color.blurple()
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )

    tree.add_command(list_dm_log_recipients)