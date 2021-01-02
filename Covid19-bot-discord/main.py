import discord
import requests
import os
from bs4 import BeautifulSoup
from keep_alive import keep_alive


client = discord.Client()

#Variables to Process
page = requests.get("https://www.worldometers.info/coronavirus/country/bangladesh/")
soup = BeautifulSoup(page.content, 'html.parser')
updates = soup.title.text
new_cases = soup.select('strong')[1].text
new_deaths = soup.select('strong')[2].text

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('Safety'):
    await message.channel.send('1) Wash your hands')
    await message.channel.send('2) Wear a mask')
    await message.channel.send('3) Use Hand Sanitizers')
    await message.channel.send('4) Stay home if you feel sick')

  
  if message.content.startswith('Info'):
    await message.channel.send('Made by Byte36')
    await message.channel.send('All Rights Reserved ® Kowsar Rahman')

  if message.content.startswith('Commands'):
    await message.channel.send('Type "Safety" to get guidelines')
    await message.channel.send('Type "Info" to know about us')
    await message.channel.send('Type "News" to get statistics')
    await message.channel.send('Regards, Byte36')

  if message.content.startswith('News'):
    await message.channel.send("Assalamu Alaikum!")
    await message.channel.send(updates)
    await message.channel.send(new_cases)
    await message.channel.send(new_deaths)
    await message.channel.send('Regards, Byte36')

  



keep_alive()
client.run(os.getenv('TOKEN'))

