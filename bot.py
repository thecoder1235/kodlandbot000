import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Giriş yapıldı: {bot.user}")

@bot.command()
async def mem(ctx):
    files = [
        "images/mem1.jpg",
        "images/mem2.jpg",
        "images/mem3.jpg",
        "images/mem4.jpg",
        "images/mem5.jpg",
        "images/mem6.jpg",
        "images/mem7.jpg"
    ]
    chosen = random.choice(files)
    with open(chosen, "rb") as f:
        await ctx.send(file=discord.File(f, filename=chosen.split("/")[-1]))

bot.run("YOUR_BOT_TOKEN_HERE")
