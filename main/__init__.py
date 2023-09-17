#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 3704772
API_HASH = "b8e50a035abb851c0dd424e14cac4c06"
BOT_TOKEN = "1064540465:AAFTgEC_xtVSiu3RdoESorVfy_cAwZ5K0Qw"
SESSION = "BQA4h8QAwnajp2P3Ycqu1ZXe-q9n0-Sz0ZY_y8Of0YdawntmdjkIUePKbT93geeWo6t3n4CxK7l7RenDhh_QxmBUh3v6Iv7Yt9EReGlbXDbKElyhxx9KlFsH6jIsQzHd2SJcqFxGpxJr5o96XLCVL4DJ3H7XnpjEQBkoG5_1N6c-N01vU5eC8XjNVZQdLobg9h-PcvpnJCxBpUHQrUbdMu_kgJMgHjZfh4diOKkEM5vBs7MaYAiVv-zLInetIdT57rKs2ZHsLYlxqx76wGQAdDwhmFzA1tpHleR2GaQ5Jimcibb-uZphWbkdU2OIEQI3dskiH44Z0Nm4301tri0mQamLdsIGagAAAAAd2TbUAA"
FORCESUB = "rootedcyberchannel2"
AUTH = 500774612

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
