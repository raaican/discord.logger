import discord
from discord.ext import commands
import config

class VoiceState(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mod = config.mod_channel

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        channel = self.bot.get_channel(self.mod)
        if before.channel is None:
            if after.channel.id is config.create:
                return
            elif after.channel.id:
                await channel.send(f"{member.mention}, joined {after.channel.mention}")

async def setup(bot):
    await bot.add_cog(VoiceState(bot))
