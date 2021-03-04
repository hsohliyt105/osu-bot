# -*- coding: utf-8 -*-

import os

import discord
from dotenv import load_dotenv

import commands

load_dotenv(encoding="UTF-8")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print("I'm on!")
    
    return
    
@client.event
async def on_message(message):
    print(f"{datetime.now()} {message.channel} {message.author} {message.content}")

    if message.author == client.user or message.author.bot:
        return

    if message.content.startswith("!"):
        string = message.content.split()

        if len(string[0]) > 1:
            string[0] = string[0][1:]
        else:
            return
    
        if message.lower() == "!Hello":
            await commands.command.hello_world()

        if message
        
    return

client.run(DISCORD_TOKEN)
