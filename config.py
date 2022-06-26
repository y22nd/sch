## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBSlQDB2te_0AkJjgJR6mM-xnYBZI3u-7syZ6t5ou_VWjPl71-U9eO9JNSUWMI_VgPtl_ba9yYyawvK6q7dAlxS3zOR2o5pdibjtO9DIZh_DoBnDe-2lvZ5QwXiUHIi_VlXH3xkwpCgzWDQYbdA5kLL0z6mJuc_KTLOK2qjhMsvnn7gD63p4Ylh-rDfQ2WcYXboEQnXYNFJRGi_q-Fv4A5mlTAFN3mIlsYMtLp8TCz6IkFaJwJ19eIjZkJxElRf2UiNhJMRCPXVe2ctE0y4HGucHGTx6sSzJ7F-wTzNaToHARuMEclAKg-deASdDE0lF5IFs2Qeybew3p0QjLNkmm-mAAAAAUY7l7MA")
BOT_TOKEN = getenv("BOT_TOKEN", "5403114400:AAEscMLyZXp0sYmJOG0qbDUDwLNFmq_pbGY")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Y_8_3")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "XIXI7bot")
OWNER_ID = getenv("OWNER_ID", "5541000365")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Paaane")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "zzcsz")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Y_8_3")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5541000365").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/6111837a4b2586e21e96c.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
