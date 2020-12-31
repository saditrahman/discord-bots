import discord
import os
import requests
import json
import random
import datetime
from keep_alive import keep_alive

client = discord.Client()


sad_words = ["sad", "depressed", "unhappy", "angry", "alone", "miserable", "broke", "cheated"]

motivate = ["You are an amazing person", "Don't loose hope!", "You are beautiful", "Allah created you in the best form!"]


dt = datetime.datetime.today()

date = str(dt.day) + "/" + str(dt.month) + "/" + str(dt.year)

hny = "01/01/2021"

##Function to get qoutes
def get_quotes():
  ##Reads from the url and then parse it before finally calling function
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " --" + json_data[0]['a']
  return quote



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  
  ##Hello Greeting
  if message.content.startswith('Hello'):
    await message.channel.send('Hello :)')
  
  ##Inspire
  if message.content.startswith('Inspire'):
    quote = get_quotes()
    await message.channel.send(quote)

  ##Info

  if message.content.startswith('Info'):
    await message.channel.send("Made by Byte36. All Rights Reserved® Kowsar Rahman Sadit :)")
  
  ##Motivate Function
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(motivate))

  if date == hny:
    await message.channel.send('Happy New Year 2021! May this year bring happiness and joy to all members -- Greetings from Byte36!')

keep_alive()
client.run(os.getenv('TOKEN'))

