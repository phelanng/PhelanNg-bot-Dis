from ast import Not
from csv import writer
import trace
from turtle import bye
import discord
from discord.ext import commands
import os  
from dotenv import load_dotenv
load_dotenv # type: ignore
import yaml
import random
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
TOKEN = os.getenv('BOT_TOKEN')

block_list = ["Lồn", "Lồn mẹ", "Lồn con", "Lồn chó", "Lồn cặc", "Lồn đít", "Lồn vú", "Lồn mông", "Lồn bướm", "Lồn trym", "Lồn lồn", "Lồn lồn lồn", "Cặc",
               "Cặc mẹ", "Cặc con", "Cặc chó", "Cặc lồn", "Cặc đít", "Cặc vú", "Cặc mông", "Cặc bướm", "Cặc trym", "Cặc cặc", "Cặc cặc cặc", "Cặc lồn lồn",
               "Địt", "Địt mẹ", "Địt con", "Địt chó", "Địt lồn", "Địt cặc", "Địt đít", "Địt vú", "Địt mông", "Địt bướm", "Địt trym", "Địt địt", "Địt địt địt", "Địt lồn lồn",
               "Địt cặc cặc", "Địt lồn cặc", "Địt lồn đít", "Địt lồn vú", "Địt lồn mông", "Địt lồn bướm", "Địt lồn trym", "Địt cặc đít", "Địt cặc vú", "Địt cặc mông",
                 "Địt cặc bướm", "Địt cặc trym",]

def read_yaml(file_path):
    with open(file_path,'r', encoding = 'utf-8') as file:
         data = yaml.safe_load(file) # type: ignore
    return data

intents = discord.Intents.default()
intents.typing = True
intents.message_content = True
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix='?', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(msg):
    if msg.author != client.user:
        for text in block_list:
            if text.lower() in msg.content.lower():
                await msg.delete()
                await msg.channel.send(f'Ê {msg.author.mention}, mày có thấy mày hỗn khi dùng từ đấy trong tin nhắn của mày không!')
                return
        if msg.content.lower().startswith("?hi"):
            await msg.channel.send(f'Chào mừng {msg.author.mention} đến với Trại Cai Nghiện!')
        if "ứng tuyển admin" in msg.content.lower():
            await msg.channel.send("Link ứng tuyển admin: https://forms.gle/encNa7ckvDfLEsdv5")
        await client.process_commands(msg)

@client.hybrid_command()
async def ping(ctx: commands.Context) -> None:  # This is a hybrid command, it can be used as a slash command and as a normal command
    await ctx.send(f"> Ping của mày đây: {round(client.latency * 1000)}ms")

client.run(TOKEN) # type: ignore
