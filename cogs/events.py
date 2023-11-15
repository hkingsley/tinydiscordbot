from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"{type(self).__name__} cog has been initialized.")

    @commands.Cog.listener()
    async def on_ready(self):
        print("on_ready event triggered.")
        print(f'Logged in as {self.bot.user.name}')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        print(f"Received message from {message.author}: {message.content}")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(f"Command error: {error}")


async def setup(bot):
    await bot.add_cog(Events(bot))
