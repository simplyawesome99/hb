import discord,os
import asyncio
from discord.ext import commands 
import requests
import json

bot = commands.Bot(command_prefix='$') 
url = os.getenv('resturl')
headers = {'content-type': "application/json",'cache-control': "no-cache"}

@bot.event
async def on_ready():
    game = discord.Activity(name="Sleeping", type=discord.ActivityType.playing)
    await bot.change_presence(status=discord.Status.dnd, activity=game)

# Commands  

@bot.command() 
async def exp(ctx,*,args):
    

    payload = json.dumps( {"type": "level","level": float(args)} )
    # api request 
    response = requests.request("POST", url, data=payload, headers=headers)
    # sends results 
    await ctx.send(response.text)
    
bot.run(os.getenv('TOKEN'))