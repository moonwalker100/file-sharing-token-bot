import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID & API HASH from my.telegram.org [https://youtu.be/gZQJ-yTMkEo?si=H4NlUUgjsIc5btzH]
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "27693340"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1056193e68c138ee16edc02578c559e1")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002413997036"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1718481517"))

#Port
PORT = os.environ.get("PORT", "8585")

#Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links
PICS = (os.environ.get("PICS", "https://envs.sh/Vx5.jpg https://envs.sh/VxL.jpg https://envs.sh/Vxc.jpg https://envs.sh/V8O.jpg https://envs.sh/V8m.jpg https://envs.sh/V8X.jpg https://envs.sh/V8y.jpg")).split() #Required

#Database 
#Database [https://youtu.be/qFB0cFqiyOM?si=fVicsCcRSmpuja1A]
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://moonwalker1092:moonwalker1234@cluster0.svrznzr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#Shortner (token system) 
# check my discription to help by using my refer link of shareus.io
# 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "https://gplinks.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "fe8aa2557a758e856f79187ee1994a88da5dbd43")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/howtodownload_naruto/140") # shareus ka tut_vid he 

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", ""))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", """<b>⚡ Hᴇʏ, {mention} ~

<blockquote expandable>I ᴀᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇ ғɪʟᴇ sʜᴀʀᴇ ʙᴏᴛ V3!\nTʜᴇ ʙᴇsᴛ ᴘᴀʀᴛ ɪs ɪ ᴀᴍ ᴀʟsᴏ sᴜᴘᴘᴏʀᴛ ʀᴇǫᴜᴇsᴛ ғᴏʀᴄᴇsᴜʙ ғᴇᴀᴛᴜʀᴇ, Tᴏ ᴋɴᴏᴡ ᴅᴇᴛᴀɪʟᴇᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴄʟɪᴄᴋ ᴀʙᴏᴜᴛ ᴍᴇ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍʏ ᴀʟʟ ᴀᴅᴠᴀɴᴄᴇ ғᴇᴀᴛᴜʀᴇs!.</blockquote></b>""")

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1480923991 5069922547 6695586027").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/Photo/anything is available on the internet. We LeakHubd or its subsidiary channel doesn't produce any of them.")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(6695586027)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
