from discord.ext import commands
from discord import app_commands, Interaction


class MessageHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.handler = None
        self.role_id = 1273793165551472692
        self.emoji = "👍"

    @app_commands.command(name="mess", description="mess")
    async def invite(self, interaction: Interaction):
        await interaction.response.send_message("React to get a role")
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

async def setup(bot):
    await bot.add_cog(MessageHandler(bot))
