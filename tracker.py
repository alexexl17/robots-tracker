import os
import hashlib
import requests
import json
from pathlib import Path
from datetime import datetime

URLS = [
    "https://yabloki.ua/robots.txt",
]

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID   = os.environ["TELEGRAM_CHAT_ID"]
