from discord import app_commands, Interaction
from discord.ext import commands
import config


class ModCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="purge", description="Purge messages")
    async def purge(self, interaction: Interaction, amount: int):
        if interaction.user.id not in config.mods:
            await interaction.response.send_message("no", ephemeral=True)
            return
        else:
            if amount < 1 or amount > 20:
                await interaction.response.send_message("Insert 1-20 amount", ephemeral=True)
                return
            else:
                await interaction.response.defer(ephemeral=True)
                await interaction.channel.purge(limit=amount)
                await interaction.followup.send("purged")
                return

    async def cog_unload(self):
        self.bot.tree.remove_command(self.purge.name)

async def setup(bot):
    await bot.add_cog(ModCommands(bot))
