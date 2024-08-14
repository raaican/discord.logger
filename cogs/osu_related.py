import sql_module.adder as adder
import sql_module.checker as checker
from discord.ext import commands
from discord import app_commands, Interaction
import requests


class OsuCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="osu_link", description="Link osu! profile")
    async def osu_link(self, interaction: Interaction, profile: str):
        i = checker.osudbfind(interaction.user.id)
        if i is not None:
            await interaction.response.send_message("You already have a profile linked", ephemeral=True)
            return
        adder.add_osu((interaction.user.id, profile))
        await interaction.response.send_message("Linked!", ephemeral=True)

    @app_commands.command(name="profile", description="Get osu! profile link")
    async def profile(self, interaction: Interaction, profile: str = None):
        if profile is None:
            i = checker.osudbfind(interaction.user.id)
            if i is None:
                await interaction.response.send_message("You don't have a profile linked please link using /osu_link", ephemeral=True)
                return
            profile = i[0]
        profile_link = f"https://osu.ppy.sh/users/{profile}"
        response = requests.get(profile_link)
        if response.status_code == 200:
            message = f"[{profile}]({profile_link})"
            await interaction.response.send_message(message)
        else:
            await interaction.response.send_message("User not found")


async def setup(bot):
    await bot.add_cog(OsuCommands(bot))
