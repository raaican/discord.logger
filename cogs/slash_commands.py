from discord.ext import commands
from discord import app_commands, Interaction
import config
import requests
from bs4 import BeautifulSoup


class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="invite", description="Get invite link")
    async def invite(self, interaction: Interaction):
        await interaction.response.send_message(f"{config.invite}")

    @app_commands.command(name="rank", description="Get osu! rank")
    async def rank(self, interaction: Interaction, username:str):
        user_name = username
        url = f"https://osu.ppy.sh/users/{user_name}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            meta_description = soup.find("meta", attrs={"name": "description"})
            meta_og_title = soup.find("meta", attrs={"property": "og:title"})
            description_content = meta_description.get("content", "")
            og_title_content = meta_og_title.get("content", "")
            await interaction.response.send_message(f"{og_title_content.split(' · ')[0]} = {description_content}")
        else:
            await interaction.response.send_message("User not found")

    async def cog_unload(self):
        self.bot.tree.remove_command(self.invite.name)
        self.bot.tree.remove_command(self.rank.name)


async def setup(bot):
    await bot.add_cog(SlashCommands(bot))
