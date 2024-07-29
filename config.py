import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = 26360430
API_HASH = "4f7076fc90ac313f59d935d4e421efed"
BOT_TOKEN = "5759235328:AAFfp7obu2dolWVSQnOU-SjT14w66R9fqtQ"
MONGO_DB_URI = "mongodb+srv://Yash1:Yash1@cluster0.jvuxh49.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))
LOG_GROUP_ID = -1001861619812
OWNER_ID = 5016109398

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/vicky0604hello/DCxMUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Learningbots79")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Learning_bots")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "821d1bf8430346b98aa98e62ceb31416")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "5fad47a0e1a340ca9cf88d9aa60b494b")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "BQGSOm4AlKIh4j2GN-YcNUVBPmP0xdR0tBvm0TnNwXG866dQqueiF596zaORzl5vnN0iApv0mCwtmHrYcC7FLlPF0Ink3qitDbOyafgPvtNoD1-cPaRqYFRf0p7n39RL6Dcxv1wyMhnLqeedrSB8c06Nxr4ZuJSVHRdupotQSRwMLnVxBs3srGog2yew8Bjil9mDz2x6QF8ZFzjVhYrMB8Semz1InZL8dUZvM3Yo041VLNhDkv89eWaQljbj5hHMB86Hgm6XwUCsbLyVplaGY25tjKXuQHzM6vEEwuP_3uAnUrQPFbu0ychwp9iV7uqHURhB0wiuSU5vL_ZrK-bemtoRHzgZjAAAAAGshcErAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
STATS_IMG_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
STREAM_IMG_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
