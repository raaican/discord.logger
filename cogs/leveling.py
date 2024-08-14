import sqlite3
from discord.ext import commands


class Leveling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(message):
        if message.author.bot:
            return

        conn = sqlite3.connect('main.db')
        cursor = conn.cursor()

        cursor.execute('SELECT xp, level from user_levels WHERE discord = ?',
                       (message.author.id,))
        result = cursor.fetchone()

        if result:
            xp, level = result
        else:
            cursor.execute('INSERT INTO user_levels(discord, xp, level) VALUES (?,?,?)',
                           (message.author.id, xp, level))

        xp += 10
        next_level_xp = level * 100

        if xp >= next_level_xp:
            level += 1
            xp = xp - next_level_xp
            await message.channel.send(f"You leveled up! {message.author.mention} {level}")

        cursor.execute('UPDATE user_levels SET xp = ?, level = ? WHERE discord = ?', (xp, level, message.author.id))
        conn.commit()
        conn.close()


async def setup(bot):
    await bot.add_cog(Leveling(bot))
