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
        await self.load_extension("cogs.reaction_assign")
        await self.load_extension("cogs.mod_slash_commands")
        await self.load_extension("cogs.osu_related")
        await self.load_extension("cogs.to_meme")
        guild = discord.Object(id=config.guild)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)
        await self.load_extension("cogs.message_delete")
        await self.load_extension("cogs.voice_state")


bot = Main()


@tasks.loop(seconds=59)
async def change_status():
    global i
    game = iter([
        discord.Activity(name="Yorushika",
                         type=discord.ActivityType.listening),
        discord.Game(name="osu!"),
        discord.Activity(name="Brazil",
                         type=discord.ActivityType.competing),
        discord.Activity(name="the Sky",
                         type=discord.ActivityType.watching),
        ])

    for i in range(random.randint(1, 4)):
        i = next(game)
    await bot.change_presence(activity=i)


@bot.event
async def on_ready():
    change_status.start()
    print(f"Logged in as {bot.user} (ID: {bot.user.id})!")
    print("===================================================")

bot.run(config.token)
