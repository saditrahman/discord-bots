import discord
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Salam'):
        await message.channel.send('Walaikum Assalam')
        await message.channel.send('May Allah Bless you!')

    if message.content.startswith('Namaz'):
        await message.channel.send('Fajr: 2 Rakah Fard + 2 Rakah Sunnah')
        await message.channel.send('Zuhr: 4 Rakah Fard + 4 Rakah Sunnah + 2 Rakah Sunnah + 2 Rakah Nafl')
        await message.channel.send('Asr: 4 Rakah Fard')
        await message.channel.send('Maghrib: 3 Rakah Fard + 2 Rakah Sunnah + 2 Rakah Nafl')
        await message.channel.send('Esha: 4 Rakah Fard + 4 Rakah Sunnah + 2 Rakah Sunnah + 2 Rakah Nafl + 3 Rakah Witr')
        await message.channel.send('Salah is the key to paradise :)')
    
    if message.content.startswith('Quran Info'):
        await message.channel.send('Language: Arabic')
        await message.channel.send('Revealed to: Prophet Muahmmed (S.A.W)')
        await message.channel.send('Chapters: 114')
        await message.channel.send('Longest Surah: Al-Bakarah')
        await message.channel.send('Shortest Surah: Al-Kauthar')
        await message.channel.send('First Surah: Al-Fatihah')
        await message.channel.send('Last Surah: An-Nas')

    if message.content.startswith('Wudhu Steps'):
       await message.channel.send(file=discord.File('Wudhu.gif'))

    if message.content.startswith('Info'):
       await message.channel.send('Made by Byte36. All Rights Reserved ® by Kowsar Rahman')

    if message.content.startswith('Commands'):
      await message.channel.send("Type 'Salam' to get a greeting!")
      await message.channel.send("Type 'Namaz' to get prayer information!")
      await message.channel.send("Type 'Quran Info' to get a summary of Quran!")
      await message.channel.send("Type 'Wudhu Steps' to get an image on how to perform it!")




keep_alive()
client.run('Nzk1Mjc2NDY5MTMxNDExNDU2.X_HA7Q.2ukHKDez5T2IX7YJUXTIQZt-OoQ')
