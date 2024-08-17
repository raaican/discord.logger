from discord.ext import commands
import sql_module.adder as adder


class ExpGain(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        discord = message.author.id
        exp_gained = 10
        new_level, previous_level = adder.add_exp(discord, exp_gained)

        if new_level > previous_level:
            await message.channel.send(f"{message.author.mention} has reached level {new_level}!")

async def setup(bot):
    await bot.add_cog(ExpGain(bot))
