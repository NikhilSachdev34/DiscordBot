import discord
import asyncio

from discord.ext import tasks, commands
from config import TOKEN, PREFIXES

client = commands.Bot(command_prefix = PREFIXES, intents=discord.Intents.all(), help_command=None) # Creates our bot

print("Hello World")

client.run(TOKEN) # Runs client