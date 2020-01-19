import discord,os
import asyncio
from discord.ext import commands 

bot = commands.Bot(command_prefix='$') 

@bot.event
async def on_ready():
    game = discord.Activity(name="Sleeping", type=discord.ActivityType.listening)
    await bot.change_presence(status=discord.Status.dnd, activity=game)

# Commands  

@bot.command() 
async def say(ctx,*,args):
    await ctx.send(args) 

@bot.command() 
async def hi(ctx):
    user = ctx.author.id
    await ctx.send("Hello "+str(user)) 

@bot.command() 
async def dothis(ctx):
    await ctx.send("Done :sunglasses:")

bot.run(os.getenv('TOKEN'))