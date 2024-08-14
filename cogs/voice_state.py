from discord.ext import commands
import config

class VoiceState(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mod = config.mod_channel

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        channel = self.bot.get_channel(self.mod)
        if member.id in config.excluded_user:
            return
        if before.channel is None:
            if after.channel.id == config.create:
                return
            elif after.channel.id:
                await channel.send(f"{member.mention} joined {after.channel.mention}")
        if after.channel is None:
            if before.channel.id == config.create:
                return
            await channel.send(f"{member.mention} left {before.channel.mention}")
        if before.channel and after.channel and after.channel.id != config.create:
            if before.channel.id == config.create:
                await channel.send(f"{member.mention} created a channel > {after.channel.mention}")
            elif before.channel.id and after.channel.id and after.channel.id != before.channel.id:
                await channel.send(f"{member.mention} switched from {before.channel.mention} to {after.channel.mention}")
            elif before.self_mute is False and after.self_mute is True:
                await channel.send(f"{member.mention} muted")
            elif before.self_mute is True and after.self_mute is False:
                await channel.send(f"{member.mention} unmuted")

async def setup(bot):
    await bot.add_cog(VoiceState(bot))
