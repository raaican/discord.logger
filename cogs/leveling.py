import discord
from discord import app_commands
from discord.ext import commands
import sqlite3
import sql_module.adder as adder

class Leveling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="level", description="Shows your level")
    async def level(self, interaction: discord.Interaction):
        discord = interaction.user.id
        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute('SELECT exp, level FROM levels WHERE discord = ?', (discord,))

        result = cur.fetchone()
        if result:
            exp, level = result
            await interaction.response.send_message(f"You are level {level} with {exp} xp")
        else:
            await interaction.response.send_message("You don't have any xp yet")

        conn.close()

    @app_commands.command(name="addxp", description="Adds xp to your profile")
    async def addxp(self, interaction: discord.Interaction, amount: int):
        discord = interaction.user.id
        adder.add_exp(discord, amount)
        await interaction.response.send_message(f"Added {amount} xp to your profile")

    @app_commands.command(name="progress", description="Shows your progress")
    async def progress(self, interaction: discord.Interaction):
        discord = interaction.user.id
        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute('SELECT exp, level FROM levels WHERE discord = ?', (discord,))
        result = cur.fetchone()

        if result is None:
            await interaction.response.send_message("You don't have any xp yet")
            return
        exp, level = result
        level_up_threshold = 100 * level

        progress = exp / level_up_threshold
        progress_bar = '==' * int(progress * 20) +  '  ' * (20 - int(progress * 20))
        progress_message = (f"Level: {level}\n"
                            f"Exp: {exp}/{level_up_threshold}\n"
                            f"Progress: [{progress_bar}] ({int(progress * 100)}%)")
        await interaction.response.send_message(progress_message)

        conn.close()

async def setup(bot):
    await bot.add_cog(Leveling(bot))


