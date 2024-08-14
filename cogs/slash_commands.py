import discord
from discord.ext import commands
from discord import app_commands, Interaction
import config


class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="invite", description="Get invite link")
    async def invite(self, interaction: Interaction):
        await interaction.response.send_message(f"{config.invite}")

    @app_commands.command(name="create", description="Create a voice channel")
    async def create(self, interaction: Interaction, name: str, category: str = config.default_category, limit: int = 0):
        guild = interaction.guild
        if interaction.user.id not in config.mods:
            await interaction.response.send_message("no")
            return
        else:
            if category:
                category_name = discord.utils.get(guild.categories, name=category)
                if not category_name:
                    category_name = await guild.create_category(name=category)
            await guild.create_voice_channel(name, category=category_name, user_limit=limit)
            await interaction.response.send_message(f"{name} created")

    @app_commands.command(name="remove", description="Remove a voice channel")
    async def remove(self, interaction: Interaction, name: str):
        if interaction.user.id not in config.mods:
            await interaction.response.send_message("no")
            return
        else:
            guild = interaction.guild
            channel = discord.utils.get(guild.voice_channels, name=name)
            if channel:
                await channel.delete()
                await interaction.response.send_message(f"{name} removed")
            else:
                await interaction.response.send_message("Channel not found")


async def setup(bot):
    await bot.add_cog(SlashCommands(bot))
