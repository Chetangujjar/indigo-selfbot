import discord
from discord.ext import commands
from main import prefix, embedColor

class Main(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='help', description='Show help menu', usage='')
    async def help(self, ctx):
        outMessage = 'Arguments in `[]` are required, arguments in `()` are optional.'
        for cog in self.client.cogs:
            outMessage += (f"\n\n__**{cog}:**__\n")
            cog = self.client.get_cog(cog)
            outMessage += '\n'.join([f'**`{prefix}`{command}{command.usage}** » {command.description}' for command in cog.get_commands()])
        await ctx.message.edit(
            content='',
            embed=discord.Embed(
                color=embedColor,
                title='Indigo - Help',
                description=outMessage
            ).set_footer(text=f'Prefix: {prefix}') 
        )
def setup(client):
    client.add_cog(Main(client))
