# -*- coding: utf-8 -*-

import os
from datetime import datetime
import json

import discord
from dotenv import load_dotenv

import functions
import commands
import helper
import translator
import preferences

load_dotenv(encoding="UTF-8")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(activity=discord.Game("!명령어 / !help"), intents=intents)

#가동시의 반응
@client.event
async def on_ready():
    print(f"{client.user}이 디스코드에 접속했어요. ")

#메시지를 받았을 때의 반응
@client.event
async def on_message(message):
    print(f"{datetime.now()} {message.channel} {message.author} {message.content}")

    if message.author == client.user or message.author.bot:
        return
    
    if functions.Identifier.is_beatmap_url(message.content):
        beatmap_id = functions.Converter.url_to_beatmap(message.content).beatmapId

        user = {'language': "en", 'osu_id': 0, 'mode': 0}

        com = commands.commands(client, message, user)

        await com.beatmap([str(beatmap_id)])
        
    if message.content.startswith("!"):
        user = preferences.load_user(message.author.id)

        if user is None:
            user = {'language': "en", 'osu_id': 0, 'mode': 0}
            com = commands.commands(client, message, user)
            
        else:
            com = commands.commands(client, message, user)

        #입력을 쪼개서 배열로 만듬
        string = message.content.split()

        if len(string[0]) > 1:
            string[0] = string[0][1:]
        else:
            return

        command = translator.alias.command(string[0])

        if command == "help":
            await com.help(string)
            return

        elif command == "beatmap":
            await com.beatmap(string)
            return

        elif command == "set":
            await com.set(string)
            return

        elif command == "recent":
            await com.recent(string)
            return

        elif command == "top":
            await com.top(string)
            return

client.run(DISCORD_TOKEN)