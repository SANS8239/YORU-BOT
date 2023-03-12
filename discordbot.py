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
from discord.utils import get

## using environment variable ##
PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

## declaration bot, intents ##
intents = discord.Intents().all()
client = commands.Bot(command_prefix='/', intents = intents)



@client.event
async def on_ready():
     await client.change_presence(status=discord.Status.online, activity=discord.Game("난 바보가 아니야... 바보가 아니라고!"))

@client.command(aliases = ['요루'])
async def yoru (ctx, url) :
     voice_channel = get(ctx.guild.voice_channels, name='음성채널이름')
     if not voice_channel:
        await ctx.send(embed = discord.Embed(description = "음.. 나에게 노래를 부르게 시키고 싶으면 음성채널에 먼저 접속해 줘!", color = 0x000000))
        return
     
    await voice_channel.connect()
    voice_client = get(bot.voice_clients, guild=ctx.guild)
     
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'nocheckcertificate': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }

     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
       info_dict = ydl.extract_info(url, download=False)
       video_title = info_dict.get('title', None)
       video_url = info_dict.get('url', None)
     
     source = await discord.FFmpegOpusAudio.from_probe(video_url)
     voice_client.play(source)
     await ctx.send(f'**{video_title}**을(를) 재생합니다.')

     
     @client.command(aliases = ['요루정지'])
     async def yoru_stop (ctx) :
          voice_client = get(bot.voice_clients, guild=ctx.guild)
          if voice_client.is_playing():
              voice_client.stop()
              await voice_client.disconnect()
              await ctx.send("노래를 정지하고 음성채널에서 나갑니다.")

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
