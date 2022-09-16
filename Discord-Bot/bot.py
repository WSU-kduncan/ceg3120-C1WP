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
        'Gus, dont be the tender sweetness of a seasick crocodile.',
        'Gus, dont be the very model of a modern major general.',
        'Gus, dont be your jury summons that I accidentally threw away last month along with something called a W-2.',
        'Gus, dont be Nic Cages accent from Con Air.',
        'Gus, dont be an old sponge with hair hanging off of it.',
        'Gus, dont be exactly half of an eleven-pound black forest ham.',
        'Gus, dont be a rabid porcupine.',
    ]
    if message.content == 'towel!':
    #if message.content.startswith('$towel'):
        response = random.choice(hitchhiker_quotes)
        await message.channel.send(response)
    
    if message.content == 'gdb!':
    #if message.content.startswith('$gdb!'):
        response = random.choice(psych_quotes)
        await message.channel.send(response)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    psych_quotes = [
        'a gooey chocolate chip cookie.',
        'an incorrigible Eskimo pie with a caramel ribbon."',
        'a rabid porcupine.',
        'exactly half of an eleven-pound black forest ham.',
        'the American adaptation of the British Gus.',
        'Nic Cage\'s accent from Con Air.',
        'your jury summons that I accidentally threw away last month along with something called a W-2.',
        'the tender sweetness of a seasick crocodile.',
        'the very model of a modern major general.',
    ]
    if message.content == 'Gus, dont be':
        response = random.choice(psych_quotes)
        await message.channel.send(response)

client.run(TOKEN)