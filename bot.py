import os
import asyncio
from pyrogram import Client

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

app = Client("my_music_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

async def main():
    await app.start()
    print("Bot muvaffaqiyatli ishga tushdi!")
    # Render "Web Service" uchun port talab qilmasligi uchun 
    # to'g'ridan-to'g'ri abadiy kutish rejimiga o'tamiz
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
