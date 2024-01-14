import disnake
from os import environ
from disnake.ext import commands

bot = commands.InteractionBot()
token = environ["token"]

@bot.slash_command(description="Sends messages anonymously")
async def send(inter, message):
    if len(message) < 2001:
     await inter.channel.send(message)

bot.run(token)
