import os, random, discord
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
            print(
        f'{client.user} connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

@client.event   
async def on_message(message):
    if message.author == client.user:
        return
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

async def send_message(message):
    await message.channel.send()
    print('Message Sent!')

def start_discord_bot(BOT_TOKEN):
    client.run(BOT_TOKEN)