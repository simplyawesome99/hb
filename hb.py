import discord,os
import asyncio
from discord.ext import commands 
import requests
import json
import re 
# Custom Request 
import cr 

bot = commands.Bot(command_prefix='$') 

# API Url 
rurl = os.getenv('resturl')

# Request Class 

mc = cr.CustomRequest(rurl)

#Events

@bot.event
async def on_ready():

    game = discord.Activity(name="Minecraft", type=discord.ActivityType.playing)
    await bot.change_presence(status=discord.Status.online, activity=game)

# Commands  

# Level To Experience 

@bot.command() 
async def xp(ctx,*,args):
    raw = re.findall(r"[-+]?\d*\.\d+|\d+",args)
    level = float(raw[0]) or 0
    if level >=0.0:
        xp = mc.getXP(level)
        embed = discord.Embed(title="> **Minecraft XP Calculator**", description="Your Result :  ", color=0xffff40)
        embed.set_footer(text='Made By @MrEinsteinReturns#0521',icon_url='')
        embed.set_thumbnail(url= os.getenv('thurl'))
        embed.add_field(name="Experience Level", value="{}".format(level), inline=False)
        embed.add_field(name="Total Experience", value="{}".format(xp), inline=False)
        # sends results 
        await ctx.send(embed=embed)
        
    else:
        await ctx.send("Only Positive Value Allowed!")
    
#Experience To Level 
@bot.command() 
async def xp(ctx,*,args):
    raw = re.findall(r"[-+]?\d*\.\d+|\d+",args)
    xp = float(raw[0]) or 0
    if xp >=0.0:
        level = mc.getXP(xp)
        embed = discord.Embed(title="> **Minecraft XP Calculator**", description="Your Result :  ", color=0xffff40)
        embed.set_footer(text='Made By @MrEinsteinReturns#0521',icon_url='')
        embed.set_thumbnail(url= os.getenv('thurl'))
        embed.add_field(name="Experience Level", value="{}".format(level), inline=False)
        embed.add_field(name="Total Experience", value="{}".format(xp), inline=False)
        # sends results 
        await ctx.send(embed=embed)
        
    else:
        await ctx.send("Only Positive Value Allowed!")
    
# Running The Bot        
bot.run(os.getenv('TOKEN'))