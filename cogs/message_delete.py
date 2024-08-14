from discord.ext import commands
import config


class MessageDelete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot or message.author.id in config.excluded_user:
            return
        channel = self.bot.get_channel(config.mod_channel)
        await channel.send(
                f"{message.author.mention} deleted: '{message.content}'"
                )


async def setup(bot):
    await bot.add_cog(MessageDelete(bot))
