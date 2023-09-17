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
SESSION = "BQA4h8QAu3xgrOaa6iNGBOy1X1FWiAqZ6JVWVFaXZgC5aTNUczrXbRzouWroPIP9M3jeBx_HDe_KkiVgjGnb9hl2epf0FZQeDVRsWRH3qMaqCdx2WMOWtord8ochlEE6LJbCZW6zG1jpmLpzkxDGC2RInBTj4QrkYxHSEtLsNfwJUvWmcAk_D_nScilRql7jI2sw6OjODyND2cWTYJ4uy6zZuhTrq2ztJwtrAskYSyFafIDyUH4LbsRt6jjH9EK7OkhKVvo2B2lZjfi5rdeKRIdzgLeFAereUF2IgVPKhZgtZhLqSYyBKbdxp-N9kiT-nIUslK-vnr4kuj8J3Zx5hojSBmIYdQAAAAAd2TbUAA"
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
