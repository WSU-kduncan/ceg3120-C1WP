# Based on example https://discordpy.readthedocs.io/en/stable/quickstart.html
import os

import discord
import random
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    hitchhiker_quotes = [
        'There is an art, it says, or rather, a knack to flying. The knack lies in learning how to throw yourself at the ground and miss.',
        'It is a mistake to think you can solve any major problems just with potatoes.',
        'In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move.',
        'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.',
    ]

    psych_quotes = [
        'the tender sweetness of a seasick crocodile.',
        'the very model of a modern major general.',
        'your jury summons that I accidentally threw away last month along with something called a W-2.',
        'Nic Cage\'s accent from Con Air.',
        'an old sponge with hair hanging off of it.',
        'exactly half of an eleven-pound black forest ham.',
        'a rabid porcupine.',
    ]
    if message.content == 'towel!':
    #if message.content.startswith('$towel'):
        response = random.choice(hitchhiker_quotes)
        await message.channel.send(response)
    
    if message.content == 'Gus, don\'t be':
    #if message.content.startswith('$gdb!'):
        response = random.choice(psych_quotes)
        await message.channel.send(response)

client.run(TOKEN)