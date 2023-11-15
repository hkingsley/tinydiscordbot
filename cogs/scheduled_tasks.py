from discord.ext import commands, tasks
import os
from datetime import datetime

class ScheduledTasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel = int(os.environ.get('DISCORD_CHANNEL_ID'))
        self.job_test.start()

    # Test Job
    @tasks.loop(minutes=1)  # runs every minute
    async def job_test(self):
        print(f"It's {datetime.now().strftime('%H:%M:%S')}! Doing the test job...")
        channel = self.bot.get_channel(self.channel)
        await channel.send(f"Sending test job Message...")

    @job_test.before_loop
    async def before_job_test(self):
        await self.bot.wait_until_ready()
    
    def cog_unload(self):
        self.job_test.cancel()

async def setup(bot):
    await bot.add_cog(ScheduledTasks(bot))
