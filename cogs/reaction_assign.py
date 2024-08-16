import discord
from discord.ext import commands
from discord import app_commands, Interaction


class MessageHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.handler = None
        self.role_id = None
        self.emoji = "👍"

    @app_commands.command(name="role", description="assign role")
    async def invite(self, interaction: Interaction, role_name: str, desc: str = "React to get a role"):
        guild = interaction.guild
        self.role_id = discord.utils.get(guild.roles, name=role_name).id
        if self.role_id is None:
            await interaction.response.send_message("Role not found")
            return

        await interaction.response.send_message(desc)
        self.handler = await interaction.original_response()
        await self.handler.add_reaction(self.emoji)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.bot:
            return
        if reaction.message == self.handler and str(reaction.emoji) == self.emoji:
            guild = reaction.message.guild
            role = guild.get_role(self.role_id)
            member = guild.get_member(user.id)
            if role and member:
                await member.add_roles(role)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if reaction.message == self.handler and str(reaction.emoji) == self.emoji:
            guild = reaction.message.guild
            role = guild.get_role(self.role_id)
            member = guild.get_member(user.id)
            if role and member:
                await member.remove_roles(role)

    @app_commands.command(name="clean_role", description="clean role message")
    async def cleaner(self, interaction: Interaction):
        await self.handler.delete()
        await interaction.response.send_message("deleted", ephemeral=True)

async def setup(bot):
    await bot.add_cog(MessageHandler(bot))
