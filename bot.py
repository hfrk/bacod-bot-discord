import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(f'Successfully logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

print('Bot started.')
client.run(os.environ['DISCORD_TOKEN'])