import discord
from discord import app_commands, Interaction
from discord.ext import commands
import config


class ModCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ann = config.announcement_channel

    @app_commands.command(name="purge", description="Purge messages")
    async def purge(self, interaction: Interaction, amount: int):
        if interaction.user.id not in config.mods:
            await interaction.response.send_message("no", ephemeral=True)
            return
        if amount < 1 or amount > 20:
            await interaction.response.send_message("Insert 1-20 amount", ephemeral=True)
            return
        await interaction.response.defer(ephemeral=True)
        await interaction.channel.purge(limit=amount)
        await interaction.followup.send("purged")
        return

    @app_commands.command(name="create", description="Create a voice channel")
    async def create(self, interaction: Interaction, name: str, category: str = config.default_category, limit: int = 0):
        if interaction.user.id not in config.mods:
            await interaction.response.send_message("no", ephemeral=True)
            return
        guild = interaction.guild
        category_name = discord.utils.get(guild.categories, name=category)
        if not category_name:
            category_name = await guild.create_category(name=category)
        await guild.create_voice_channel(name, category=category_name, user_limit=limit)
        await interaction.response.send_message(f"{name} created by {interaction.user.mention}")

    @app_commands.command(name="remove", description="Remove a voice channel")
    async def remove(self, interaction: Interaction, name: str):
        if interaction.user.id not in config.mods:
            await interaction.response.send_message("no", ephemeral=True)
            return
        guild = interaction.guild
        channel = discord.utils.get(guild.voice_channels, name=name)
        if channel is None:
            await interaction.response.send_message("Channel not found", ephemeral=True)
            return
        await channel.delete()
        await interaction.response.send_message(f"{name} removed by {interaction.user.mention}")

    @app_commands.command(name="announce", description="send an announcement")
    async def announce(self, interaction: Interaction, announcement: str):
        channel = self.bot.get_channel(self.ann)
        if interaction.user.id not in config.mods:
            await interaction.response.send_message("no", ephemeral=True)
            return
        await channel.send(announcement)
        await interaction.response.send_message("announcement sent", ephemeral=True)

async def setup(bot):
    await bot.add_cog(ModCommands(bot))
