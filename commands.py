# -*- coding: utf-8 -*-

import os
import datetime
import time
import random
import json

import discord

class commands:
    def __init__(self, client, message, user):
        self.client = client
        self.message = message
        self.user = user
        
        return
        
    def hello_world(self):
        self.message.channel.send("Hello world!")
        
        return

    def current_time(self):
        time_now = datetime.time
        self.message.channel.send(f"The time now is {time_now}.")
