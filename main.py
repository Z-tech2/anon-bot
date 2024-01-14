import disnake
from disnake.ext import commands

bot = commands.InteractionBot()
token = "PUT BOT TOKEN HERE"

@bot.slash_command(description="Sends messages anonymously")
async def send(inter, message):
    if len(message) < 2001:
     await inter.channel.send(message)

bot.run(token)
