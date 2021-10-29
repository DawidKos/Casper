from algorithms import *
from dotenv import load_dotenv  # pip install python-dotenv
from os import environ
import random
from discord_components import Button

########################################################################################################################
load_dotenv()
DISCORD_TOKEN = environ.get('DISCORD_TOKEN')  # Przypisanie DISCORD_TOKEN ze zmiennych środowiskowych
client = discord.Client()  # obiekt reprezentujący połączenie z discordem
casper_id = '<@!853645195802181672>'  # id caspra
interaction_channels = ('testy', '🤖・poligon', '👻・casper-bot')  # kanały aktywności bota


# Link do repozytorium: https://github.com/DawidKos/Casper.git
# Poradnik o podstawach discord bota https://realpython.com/how-to-make-a-discord-bot-python/
# GitHub biblioteki discord.py: https://github.com/Rapptz/discord.py
# Dokumentacja discord.py https://discordpy.readthedocs.io/en/latest/api.html
# Metody obiektu message: https://discordpy.readthedocs.io/en/latest/api.html#discord.Message

########################################################################################################################

from casper import Casper

bot = Casper()

@client.event
async def on_ready():  # on_ready() wywoływane po połączeniu z discordem
    print(f'{client.user.name} connected')
    print(f'Bot ID: {client.user.id}')


@client.event
async def on_message(message):  # on_message() wywoływane po nadejściu wiadomości
    await message.channel.send(
        bot.on_message(casper_id, message)
    )


client.run(DISCORD_TOKEN)
