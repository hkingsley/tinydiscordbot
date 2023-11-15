import os
import asyncio
import discord
from discord.ext import commands
from config import settings

async def load_extensions(bot):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            print(f"Loading cog {filename}...")
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f"Loaded cog {filename}.")

async def main():
    bot = commands.Bot(command_prefix='!', intents=settings.INTENTS)

    # Load cogs
    await load_extensions(bot)

    # Check if the token is valid
    if not settings.BOT_TOKEN:
        print('Bot token is missing.')
    else:
        try:
            # Run the bot
            await bot.start(settings.BOT_TOKEN)
        except discord.errors.LoginFailure:
            print('Improper token has been passed.')

if __name__ == '__main__':
    asyncio.run(main())
