# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
🏷 Hi,👋 I'm a Permanent Files Store Bot!
Send me any file I will save it in my Large Database.\n\n📜 **My Features**💡\n• I Store Files Permanent.\n• Unlimited Files,Any Size.\n• I Support any Kind of files.\n• With Thumbnail & Caption.\n• I Remove Forward Tag also.\n\n**You Not need to Worry for your files**.😊

🤖 **My Name:** [Filє Sтσяє Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Creator:** [This Person](https://t.me/Krsna)

🤗 **Thanks To:** [Linux Repositories](https://t.me/linux_repo)

🚶**About Dev:** [Click Here](https://t.me/HKrrish)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Dev:** [This Person](https://t.me/Krsna)

I'm not a Professional Dev, Super Noob. Just Learning from Official Docs. Please Don't Misuse the Bot!

📍**Remember**\n• If Bot Stop, Don't Worry your files not go anywhere. Just Check Status. 👇\n• Don't Send Useless, Adults Files.\n• Don't Spam (Do one by one).\n\n 🤖 **Bot Status** : [Check here](https://telegra.ph/File-Store-Bot-05-10)\n\nWant Any help, Contact Me.👇 

🤖 [Contact](https://t.me/KrAsst_Bot) [#NoPm]
"""
	HOME_TEXT = """
Hey!, [{}](tg://user?id={}) 👋\n\nYou are Right Place.😊\n\nI'm a Permanent **File Store Bot**.

💡 Send me any file I will give you a permanent Shareable Link.\n\n• Check **Know More** Button.👇\n\nThank You :)
"""
