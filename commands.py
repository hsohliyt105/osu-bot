# -*- coding: utf-8 -*-

import os
import datetime
import shutil
import math
from enum import Enum
import pathlib
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
