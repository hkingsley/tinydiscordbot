# config/settings.py
import os
import discord

BOT_TOKEN = os.environ.get('BOT_TOKEN')
INTENTS = discord.Intents.default()
INTENTS.message_content = True
