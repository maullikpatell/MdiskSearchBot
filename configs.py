# (c) @RoyalKrrishna

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 8143783))
    API_HASH = os.environ.get("API_HASH", "889c67efa7cf3979acc079c3271f4254")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5732195902:AAHFTEHpnBscXnyDDsBb-HCTpXuNYLngpSI")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "dtglinks")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQC1oeyZH--GAVkesYYKkg1lhqIVHDL4MOh2LY6tGNINfXZWfNxmkrsQkXfqAvToERWgBaup5M7NfjyZU0YC0NdtFsr2dd1b31mLfqTZCfBCsFjAafViyivfdQTBaOtyTXCA3HFmwOku0XvT-0d7GeSGuTcqKBoON0gR3AQT3rRG9aecIGD41s2GNoSsCtc5qqUClYebCYzUaR2H-riAesnkxqbwfutcYbrZC-qsKPgIdRX_I1ham8UnX9YQ7PttUcK72jKGOUL8YL7uLRaKTZo_a61j8Ex2ltgkoTarMoEym0uOrrU69L9FxOjZ73jCKaslbLHmHY20Q9iL4Y0Y7IHNbOWCDAA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001395650746)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", DTG_LINKS_BOT)
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 788277212))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/DTG_BOTS'>DTG LINKS BOT</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://railway.app'>Railway</a>

👨‍💻 Created By: <a href='https://t.me/DTG_BOTS'>DTG BOTS</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/DTG_ADMIN_BOT'>Click Me</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm DTG LINKS BOT.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With 🔥 @DTG_BOTS </a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm DTG LINKS BOT.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With 🔥 @DTG_BOTS</a></b>
"""


