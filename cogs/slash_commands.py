from discord.ext import commands
from discord import app_commands, Interaction
import config
import requests


class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="invite", description="Get invite link")
    async def invite(self, interaction: Interaction):
        await interaction.response.send_message(f"{config.invite}")

    @app_commands.command(name="profile", description="Get osu! profile link")
    async def profile(self, interaction: Interaction, profile: str):
        profile_link = f"https://osu.ppy.sh/users/{profile}"
        response = requests.get(profile_link)
        if response.status_code == 200:
            message = f"[{profile}]({profile_link})"
            await interaction.response.send_message(message)
        else:
            await interaction.response.send_message("User not found")

    async def cog_unload(self):
        self.bot.tree.remove_command(self.invite.name)
        self.bot.tree.remove_command(self.profile.name)


async def setup(bot):
    await bot.add_cog(SlashCommands(bot))
