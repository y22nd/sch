## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCXWgN9L4fQP-jCdVzSxrJn5rr2REZjA2I2zcGBXeAC5E6GAMXAsi5K9kjEK_5EHUXNmnnyE6Q45g3UlVKUyXKbEowqDhr0t7UY2xYEWqfG4SiDOp-W7aMXGUjCWIK1j0DZgmFmDRju5qQntdkbgn6MhlHwewulnkI03QfO1M_8Q-xjocO-InApQS2jSjnAAVA1IdLjUZUJFahzXNMGmCGE4XZzSDBDMM_JgP9Lgz7dUIb2zOCGbgBA3kbKC785CwoSrXPs7UeJ6LL_RNwQCH3OCIlUwv2yxAvaK9_EHvFgMw_GrfTSoOP9uiSqr0tL6ocfu0g65aGx5ypPNBxo3lBJAAAAAUrqj_gA")
BOT_TOKEN = getenv("BOT_TOKEN", "5449892843:AAGNKvlvJKy0o0tLp76uy20aF-sUmneamL8")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "xvxvxo")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "TiGexbot")
OWNER_ID = getenv("OWNER_ID", "5309661923")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Paaane")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "F84RF")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xvxvxo")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5309661923").split()))
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
