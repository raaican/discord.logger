#!./venv/bin/python3

import discord
from discord.ext import commands
import config


class Main(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="r!", intents=discord.Intents.all())

    async def setup_hook(self):
        await self.load_extension("cogs.slash_commands")
        guild = discord.Object(id=config.guild)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)


bot = Main()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("===================================================")

bot.run(config.token)
