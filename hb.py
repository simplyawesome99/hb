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

    game = discord.Activity(name="Development", type=discord.ActivityType.playing)
    await bot.change_presence(status=discord.Status.online, activity=game)

# Commands  

# mclevel To Experience 

@bot.command(aliases=['exp','fromlevel','toxp']) 
async def xp(ctx,*,args):
    raw = re.findall(r"[-+]?\d*\.\d+|\d+",args)
    mclevel = float(raw[0]) or 0
    if mclevel >=0.0:
        mcxp = mc.getXP(mclevel)
        embed = discord.Embed(title="> **Minecraft XP Calculator**", description="Your Result :  ", color=0xffff40)
        embed.set_footer(text='Made By @MrEinsteinReturns#0521',icon_url='')
        embed.set_thumbnail(url= os.getenv('thurl'))
        embed.add_field(name="Experience Level", value="{}".format(mclevel), inline=False)
        embed.add_field(name="Total Experience", value="{}".format(mcxp), inline=False)
        # sends results 
        await ctx.send(embed=embed)
        
    else:
        await ctx.send("Only Positive Value Allowed!")
    
#Experience To MClevel 
@bot.command(aliases=['lv','fromxp','tolevel']) 
async def mclevel(ctx,*,args):
    raw = re.findall(r"[-+]?\d*\.\d+|\d+",args)
    mcxp = float(raw[0]) or 0
    if mcxp >=0.0:
        mclevel = mc.getLevel(mcxp)
        embed = discord.Embed(title="> **Minecraft XP Calculator**", description="Your Result :  ", color=0xffff40)
        embed.set_footer(text='Made By @MrEinsteinReturns#0521',icon_url='')
        embed.set_thumbnail(url= os.getenv('thurl'))
        embed.add_field(name="Experience Level", value="{}".format(mclevel), inline=False)
        embed.add_field(name="Total Experience", value="{}".format(mcxp), inline=False)
        # sends results 
        await ctx.send(embed=embed)
        
    else:
        await ctx.send("Only Positive Value Allowed!")
    
# Running The Bot        

bot.run(os.getenv('TOKEN'))