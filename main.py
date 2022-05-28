import os
import discord
from discord.ext import commands

#------------------token goes here
token=""
prefix=""
messagedm="This Message is going to your dm"

#------------------start
client = commands.Bot(command_prefix=prefix, self_bot=True, fetch_offline_members=False)
@client.event
async def on_ready():
    print('Ready as: {0.user}'.format(client))

#------------------dm private
@client.event
async def on_message(message):
  msg = message.content

  if 'e' or 'a' or 'i' or 'o' or 'U' or 'E' or 'A' or 'I' or 'O' or 'U' in msg:
    await message.author.send(messagedm)

#------------------run
client.run(token, bot=False)