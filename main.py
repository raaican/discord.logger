#!./venv/bin/python3

import discord
import random
from discord.ext import commands
import config
from discord.ext import tasks


class Main(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="r!", intents=discord.Intents.all())

    async def setup_hook(self):
        await self.load_extension("cogs.slash_commands")
        await self.load_extension("cogs.mod_slash_commands")
        await self.load_extension("cogs.osu_related")
        guild = discord.Object(id=config.guild)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)
        await self.load_extension("cogs.message_delete")
        await self.load_extension("cogs.voice_state")


bot = Main()


@tasks.loop(seconds=59)
async def change_status():
    activities = [
        discord.Game(name="Listening to /invite"),
        discord.Game(name="Listening to /osu_link"),
        discord.Game(name="Listening to Server activity"),
    ]

    activity = random.choice(activities)
    await bot.change_presence(activity=activity)


@bot.event
async def on_ready():
    change_status.start()
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("===================================================")

bot.run(config.token)
