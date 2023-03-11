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
sensivity = 1

sensivity_1 = ['ㅆㅂ', '씨발', 'ㄱㅅㄲ', '개새끼', '니애미', '니애비', '느금마', '느금', '병신', 'ㄴㄱㅁ', 'Tlqkf', 'qudtls', 'rotoRl']

sensivity_2 = ['ㅆㅂ', '씨발', 'ㄱㅅㄲ', '개새끼', '니애미', '니애비', '느금마', '느금', '병신', 'ㄴㄱㅁ', 'Tlqkf', 'qudtls', 'rotoRl', 'tlqkf', 'qud', 'rotorl', 'ㅅㅂ', 'ㅈㄹ', '지랄', '튀르이', 'ㅌㄹㅇ', '좆같', 'ㅈ같']

sensivity_3 = ['ㅆㅂ', '씨발', 'ㄱㅅㄲ', 'ㄳㄲ', '개새끼', '니애미', '니애비', '느금마', '느금', '병신', 'ㄴㄱㅁ', 'Tlqkf', 'qudtls', 'rotoRl', 'tlqkf', 'qud', 'rotorl', 'ㅅㅂ', 'ㅈㄹ', '지랄', '튀르이', 'ㅌㄹㅇ', '시발', 'ㅄ', 'ㅂㅅ']


@client.event
async def on_ready():
     await client.change_presence(status=discord.Status.online, activity=discord.Game("난 바보가 아니야... 바보가 아니라고!"))

@client.event
async def on_message(message) :
    global sensivity
    if message.content.startswith("/요루감도조절") and str(message.author) == "米津玄師(よねづけんし)#9185":
        sensivity_input = str(message.content[8:])
        if sensivity_input == '1' : 
            sensivity = 1
            await message.channel.send(f"성공적으로 검열 수준을 {sensivity_input}로 변경 했어!")
        elif sensivity_input == '2':
            sensivity = 2
            await message.channel.send(f"성공적으로 검열 수준을 {sensivity_input}로 변경 했어!")
        elif sensivity_input == '3' :
            sensivity = 3
            await message.channel.send(f"성공적으로 검열 수준을 {sensivity_input}로 변경 했어!")
        else :
            await message.channel.send(f"감도 조절은 1 ~ 3 까지 사이의 수준으로 조정해줘! (숫자가 높을 수록 검열 강도도 up)")
    if sensivity == 1 : 
        if message.content in sensivity_1 :
            for word1 in sensivity_1 :
                if world1 in message.content
                    await message.delete()
                    await message.channel.send(embed = discord.Embed(description = f"{message.author}! 감히 내 앞에서 욕을 해?", color = 0x000000))
        
    elif sensivity == 2 : 
        if message.content in sensivity_2 :
            for word2 in sensivity_2 :
               if word2 in message.content :
                   await message.delete()
                   await message.channel.send(embed = discord.Embed(description = f"{message.author}! 감히 내 앞에서 욕을 해?", color = 0x000000))

    elif sensivity == 3 : 
        if message.content in sensivity_3 :
            for word3 in sensivity_3 :
                if word3 in message.content :
                    await message.delete()
                    await message.channel.send(embed = discord.Embed(description = f"{message.author}! 감히 내 앞에서 욕을 해?", color = 0x000000))  
           

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
