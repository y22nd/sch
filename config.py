## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgAqtXdAEojPnkH_VorkGjaDTvLHBcnSYDza5u5ONxOAP4Lvovf_mqq3atBTwYG95KfsUd09GMkxHV3W6J8I2odNTJxjTTziM6FIzSvfbPdKj3YuC7FRqgl2L5JIdKNNB300hpn6IhD7L3jSfgMlL7_dVeK-WIZB8yerUz_XZGxDzCY_SQFNq6Z4v7Yl3ZIk1JyRFQs5dSb43mj8-aGi9uM1iLF3JrD6RQAjAtQNhfytpVEBhS90KPg-gdDFUaBgud98CHhIem86La5Z6PK1hsBxfBCBlMqKqESWQ1OVvcp7fPl67DQP8S8QsMjPcCSk8GFvpQPC07xarSj4mhJ3HWesAAAAAUxAjXsA")
BOT_TOKEN = getenv("BOT_TOKEN", "5585491116:AAHuArt-ypiCLYpVn8BN6XiPVKk6LHJ_tfQ")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "TTUT2")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "musicjesusbot")
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
