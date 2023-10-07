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
SESSION = "BQA4h8QAeEEDR0NF9kXfJ4xv03GtN7VIE0tisF0N-tq4kaKajFiE5JfCE1c_WFWSv_6WKNFHB6VNlH5AqUbrojSGBdpiIB448q1xcNeJQqCAIVGLELdCAywIOFmnkbqu-U5PkGYxwLZ9kvQ9d2uUuKknKVpifeneMVRItlyEWyysdXLbJ0f_Pkc1wuazMzlvhsKlywFRFu1hc6DbMhtok_6vPijzknSSLSuv3uPixIU6G7cpo4XmtNNQxnVfd75xfao-z75srnIvv5AUbFxjIww2-pSiyG-i1EoxQKSQurXfkiM_GXlo-xZv8vEXRehelzvizelZssCDu-4xyDGrKNK0ro99tAAAAAAd2TbUAA"
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
