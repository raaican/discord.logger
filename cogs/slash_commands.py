from discord.ext import commands
from discord import app_commands, Interaction
import config


class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def invite(self, interaction: Interaction):
        await interaction.response.send_message(f"{config.invite}")

    async def cog_unload(self):
        self.bot.tree.remove_command(self.invite.name)


async def setup(bot):
    await bot.add_cog(SlashCommands(bot))
