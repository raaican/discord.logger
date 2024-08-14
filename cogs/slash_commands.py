from discord.ext import commands
from discord import app_commands, Interaction
import config


class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="invite", description="Get invite link")
    async def invite(self, interaction: Interaction):
        await interaction.response.send_message(f"{config.invite}")


async def setup(bot):
    await bot.add_cog(SlashCommands(bot))
