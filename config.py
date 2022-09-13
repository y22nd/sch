## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCu5a2Btu6Dap3XmNawe40_JgSQgphOboei-D_HkSlez0CO8I3SvoAsODHSNhmYaP4zG07FIHP8tyy7mcfHdINESavpb53_W8r_Ii8r_3aOE9dX-gj3D8jg0qpO7sExK6rc3PYfS9QCaej24FPI_WT_3vRMkEPQjDy9uh3tCyImraq1RC9Xn4XiOgZPuvKUTE0lquz9QIOz9VM83KGDP-f4A1_LrCQTYqfZWzyYyP6leIeA8azJYpGf4pSOCLdPlLAhLfpy5nPOP2yHXBcOOwxrlcU9SaTvazJWQb8c5Id7Ll59wXNV1jNb717q3PAgT77of05KyrjTDCZGTmzfA81bAAAAAUmI9LoA")
BOT_TOKEN = getenv("BOT_TOKEN", "5765934042:AAEqDgV3pYkl29gY0-Qk4lw44LzoNYEFNio")
BOT_NAME = getenv("BOT_NAME", "𝗺𝘂𝘀𝗹𝗰 𝗯𝗼𝘁")
API_ID = int(getenv("API_ID","14945425"))
API_HASH = getenv("API_HASH", "83fba9e56d99d3fe7dd9f843189d202b")
OWNER_NAME = getenv("OWNER_NAME", "𝑦𝑜𝑢𝑠𝑖𝑓 𝑎𝑏𝑎𝑠")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@y0_2n")
ALIVE_NAME = getenv("ALIVE_NAME", "")
BOT_USERNAME = getenv("y02nmbot", "")
OWNER_ID = getenv("5528679610", "")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
GROUP_SUPPORT = getenv("https://t.me/ynfbsa", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5528679610").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
