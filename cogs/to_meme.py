import config
from discord.ext import commands
from functions.meme_case import memes

class Meme(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="meme")
    async def meme(self, ctx: commands.Context):
        if ctx.author.id not in config.mods:
            return
        if not ctx.message.reference:
            print("no reference")
            return

        ref = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        result = memes(ref.content)
        await ctx.send(result, reference=ctx.message.reference)
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(Meme(bot))

