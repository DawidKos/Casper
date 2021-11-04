import discord
from dotenv import load_dotenv  # pip install python-dotenv
from os import environ
# from discord_components import Button
from algorithms.watson import Watson

########################################################################################################################
load_dotenv()
DISCORD_TOKEN = environ.get('DISCORD_TOKEN')  # Przypisanie DISCORD_TOKEN ze zmiennych środowiskowych
casper = discord.Client()  # obiekt reprezentujący połączenie z discordem
interaction_channels = ('testy', '🤖・poligon', '👻・casper-bot')  # kanały aktywności bota


# Link do repozytorium: https://github.com/DawidKos/Casper.git
# Poradnik o podstawach discord bota https://realpython.com/how-to-make-a-discord-bot-python/
# GitHub biblioteki discord.py: https://github.com/Rapptz/discord.py
# Dokumentacja discord.py https://discordpy.readthedocs.io/en/latest/api.html
# Metody obiektu message: https://discordpy.readthedocs.io/en/latest/api.html#discord.Message

########################################################################################################################


@casper.event
async def on_ready():  # on_ready() wywoływane po połączeniu z discordem
    print(f'{casper.user.name} connected')
    print(f'Bot ID: {casper.user.id}')


@casper.event
async def on_message(message):  # on_message() wywoływane po nadejściu wiadomości
    msg = Watson(message)
    print(f'({msg.channel}) {msg.author}: {msg.message}')  # Print wszystkich nadchodzących wiadomości

    if message.author.bot is not True and str(message.channel) in interaction_channels and type(msg.action) is not None:

        await message.channel.send("ok")


casper.run(DISCORD_TOKEN)
