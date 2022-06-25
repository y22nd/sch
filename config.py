## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgC_y30An-vJ_FgWhdt6uh4L8x4yRlfDYM5xtJIfLTVSfjSW4qlB9amsmaur1mRH0YPTKLVOy5bGnwj4OhJ9-JO3zBgvL3ONxTq_mFYlp79i51oXejJ7xfCQT-uXosSz4wP39kz9Nqh_60-HSuKzXHHmk4lfowUKuGMH_cvwidpeesyJO4bo9ALlbk5t5lnFtnRYK205azc318uGm3mYSZLSN_t9RnC-pZvSCM-jxtk0Ath4KPDZUvyL1KopxacVgl7z_Y2LFeoIakX8qURKbbj7eC-uWMkl3jhndeEU0i9t395T7XUGdcEbSKCgaalUZB1kFBYbrEiaN9mRGWM-YnY9-kURdQAAAAFMQI17AA")
BOT_TOKEN = getenv("BOT_TOKEN", "5223180967:AAFq_l70nFaUAtZeLGaceFE0m9e2ccmU41k")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "TTUT2")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "Micclallbot")
OWNER_ID = getenv("OWNER_ID", "1421137574")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Paaane")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TTUT2")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "IEBIE")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1421137574").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
