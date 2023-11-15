from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"{type(self).__name__} cog has been initialized.")

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello, World!')

async def setup(bot):
    await bot.add_cog(Commands(bot))


