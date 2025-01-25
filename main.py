import discord
import asyncio

from data import *
from commands import *

from discord.ext import tasks, commands
from config import *

client = commands.Bot(command_prefix = PREFIXES, intents=discord.Intents.all(), help_command=None) # Creates our bot

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def register(ctx):
    if getUser(ctx.author.id) is None:
        createUser(ctx.author.id, ctx.author.name)
        await ctx.reply(f"Hello, {ctx.author.name}!")
    else:
        await ctx.reply("Account already created.")
    

@client.command()
@commands.cooldown(1,5, commands.BucketType.user)
async def axe(ctx):
    await getResource(ctx, "axe")

@client.command()
@commands.cooldown(1,5, commands.BucketType.user)
async def sword(ctx):
    await getResource(ctx, "sword")

@client.command()
@commands.cooldown(1,5, commands.BucketType.user)
async def pickaxe(ctx):
    await getResource(ctx, "pickaxe")

async def getResource(ctx, typeOfTool):
    if getUser(ctx.author.id) is not None:
        resource = None
        userTiers = getUserTools(ctx.author.id)

        if typeOfTool == "axe": 
            resource = await axeC(ctx)
            tier = userTiers[1]
        elif typeOfTool == "sword": 
            resource = await swordC(ctx)
            tier = userTiers[2]
        elif typeOfTool == "pickaxe": 
            resource = await pickaxeC(ctx)
            tier = userTiers[3]

        await ctx.reply(embed=await resourceEmbedBuilder(typeOfTool, tier, resource))
    else:
        await ctx.reply("You do not have an account! Please register.")

async def resourceEmbedBuilder(typeOfTool, tier, gainedResources):
    if typeOfTool == "axe": 
        colour=0x25C238
        lootTableToUse = AXE_LOOT
    elif typeOfTool == "sword": 
        colour=0xE14826
        lootTableToUse = SWORD_LOOT
    elif typeOfTool == "pickaxe": 
        colour=0x808080
        lootTableToUse = PICKAXE_LOOT
    
    toolMaterial = TOOL_TIERS[tier//2] 
    if tier % 2 != 0: toolMaterial = "Enchanted " + toolMaterial

    i = 0
    resourcesString = ""
    while i < len(lootTableToUse):
        resourcesString += str(gainedResources[i]) + " " + lootTableToUse[i] + "\n"
        i += 1

    screen=discord.Embed(title = f"You used your {toolMaterial} {typeOfTool} and found: ", description=resourcesString, color=colour)
    if typeOfTool == "axe": screen.set_thumbnail(url=AXE_IMG_RESOURCES[tier])
    elif typeOfTool == "sword": screen.set_thumbnail(url=SWORD_IMG_RESOURCES[tier])
    elif typeOfTool == "pickaxe": screen.set_thumbnail(url=PICKAXE_IMG_RESOURCES[tier])

    return screen

print("ON")
client.run(TOKEN) # Runs client
#test3