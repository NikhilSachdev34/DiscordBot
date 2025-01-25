import asyncio
import random
from data import *

async def axeC(ctx):
    wood = random.randint(0,10)
    if wood > 0:
        updateUserResources(ctx.author.id, "wood", wood)
    temp = []
    temp.append(wood)
    return temp

async def swordC(ctx):
    string = random.randint(0,10)
    if string > 0:
        updateUserResources(ctx.author.id, "string", string)
    temp = []
    temp.append(string)
    return temp

async def pickaxeC(ctx):
    stone = random.randint(0,10)
    if stone > 0:
        updateUserResources(ctx.author.id, "stone", stone)
    temp = []
    temp.append(stone)
    return temp
