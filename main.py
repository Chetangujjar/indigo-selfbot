import discord, discum, json, os, sys, base64, asyncio, random, time
from discord.ext import commands
from colorama import Fore, init
from utils import *

sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=37, cols=100))

init()

try:
    config = json.load(open('config.json'))
    accountToken = config.get('ODc1NDAwNzk2MTQ4MjI0MDYw.YgUOyw.f3O7xMIf5RoBA1vVw6YU6bvEgl0')
    prefix = config.get('+')
    embedColor = int(config.get('Embed Color').replace('#', '0x'), 0)
    nitroSniper = config.get('Nitro Sniper')
except Exception as e:
    logging.printError(f'Failed to load config. Exception: {e}')
    while True: time.sleep(150)

client = discord.Client()
client = commands.Bot(
    command_prefix=prefix,
    case_insensitive=True,
    help_command=None,
    auto_reconnect=True,
    self_bot=True
)

# Credits to Lucas on YouTube
for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        try:
            client.load_extension(f'cogs.{file[:-3]}')
        except Exception as e:
            logging.printError(f'Failed to load the {file} cog. Exception: {e}')
try:
    client.run(accountToken)
except Exception as e:
    logging.printError(f'Failed to login. Exception: {e}')
