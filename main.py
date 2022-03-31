import discord
import os

TOKEN = os.environ.get('TOKEN')

Kima = discord.Bot()

@Kima.event
async def on_ready():
    print(f"We have logged in as {Kima.user}")

@Kima.slash_command()
async def hello(ctx):
    await ctx.respond("Hello!")

Kima.run(TOKEN)
