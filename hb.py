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

    game = discord.Activity(name="Minecraft", type=discord.ActivityType.playing)
    await bot.change_presence(status=discord.Status.online, activity=game)

# Commands  

# Level To Experience 
@bot.command() 
async def xp(ctx,*,args):
    if args >= 0:
        payload = json.dumps( {"type": "level","level": float(args)} )
        # api request 
        res = requests.request("POST", url, data=payload, headers=headers)
    
        data = json.loads(res.text)
        # Embed 
        embed = discord.Embed(title="> **Minecraft XP Calculator", description="Here is your Result ", color=0xffff40)
        embed.set_thumbnail(url=os.getenv('thurl'))
        embed.add_field(name="Experience Level", value="{}".format(args), inline=False)
        embed.add_field(name="Total Experience", value="{}".format(data["xp"]), inline=False)
        # sends results 
        await ctx.send(embed=embed)
    else:
        await ctx.send("Only Positive Value Allowed!")            
    
#Experience To Level 
@bot.command() 
async def level(ctx,*,args):
    if args >= 0:
        payload = json.dumps( {"type": "xp","xp": float(args)} )
        # api request 
        res = requests.request("POST", url, data=payload, headers=headers)
    
        data = json.loads(res.text)
        # Embed 
        embed = discord.Embed(title="> **Minecraft XP Calculator", description="Here is your Result ", color=0xffff40)
        embed.set_thumbnail(url=os.getenv('thurl'))
        embed.add_field(name="Experience Level", value="{}".format(data["level"]), inline=False)
        embed.add_field(name="Total Experience", value="{}".format(args), inline=False)
        # sends results 
        await ctx.send(embed=embed)
    else:
        await ctx.send("Only Positive Value Allowed!")
             

# Running The Bot        
bot.run(os.getenv('TOKEN'))