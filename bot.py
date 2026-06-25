import os
from pyrogram import Client

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

app = Client("my_music_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Port muammosini chetlab o'tish uchun oddiy usul
if __name__ == "__main__":
    app.run()
