from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()
import asyncio
from discord.ext import commands
import time 
from youtube_dl import YoutubeDL
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get 
from discord import FFmpegPCMAudio
from random import *
import urllib.request
import requests
import os
import subprocess
import pytube as pt
import glob

## using environment variable ##
PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

## declaration bot, intents ##
intents = discord.Intents().all()
client = commands.Bot(command_prefix='/', intents = intents)



@client.event
async def on_ready():
     await client.change_presence(status=discord.Status.online, activity=discord.Game("난 바보가 아니야... 바보가 아니라고!"))


           

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
