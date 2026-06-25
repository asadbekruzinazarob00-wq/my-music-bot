import os
from pyrogram import Client

# Render'dan o'qib olish
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

# Agar qiymatlar topilmasa, xato chiqarmasligi uchun tekshiramiz
if not api_id or not api_hash or not bot_token:
    print("XATO: Muhit o'zgaruvchilari (Environment Variables) to'g'ri o'rnatilmagan!")
    exit(1)

# api_id ni raqamga o'giramiz
app = Client("my_music_bot", api_id=int(api_id), api_hash=api_hash, bot_token=bot_token)

print("Bot ishga tushishga tayyor...")

if __name__ == "__main__":
    app.run()
