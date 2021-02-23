# -*- coding: utf-8 -*-

import os

import discord
from dotenv import load_dotenv

load_dotenv(encoding="UTF-8")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print("I'm on!")
    
    return
    
@client.event
async def on_message(message):
    if message.lower() == "!Hello":
        await message.channel.send(f"Hello {message.author}!")
        
    return

client.run(DISCORD_TOKEN)
