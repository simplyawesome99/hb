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

# Level To Experience 
@bot.command() 
async def exp(ctx,*,args):
    payload = json.dumps( {"type": "level","level": float(args)} )
    # api request 
    res = requests.request("POST", url, data=payload, headers=headers)
    
    data = json.loads(res.text)
    # Embed 
    embed = discord.Embed(title=str(ctx.author), description="", color=0x0000ff)
    embed.add_field(name="Level", value="{}".format(args), inline=False)
    embed.add_field(name="Experience", value="{}".format(data["xp"]), inline=False)
    # sends results 
    await ctx.send(embed=embed)
    
#Experience To Level 
     
@bot.command() 
async def level(ctx,*,args):
    payload = json.dumps( {"type": "xp","xp": float(args)} )
    # api request 
    res = requests.request("POST", url, data=payload, headers=headers)
    
    data = json.loads(res.text)
    # Embed 
    embed = discord.Embed(title=str(ctx.author), description="", color=0x0000ff)
    embed.add_field(name="Level", value="{}".format(data["level"]), inline=False)
    embed.add_field(name="Experience", value="{}".format(args), inline=False)
    # sends results 
    await ctx.send(embed=embed)
    
bot.run(os.getenv('TOKEN'))