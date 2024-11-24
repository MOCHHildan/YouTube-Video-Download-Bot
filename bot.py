# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot



from pyrogram import Client, filters
from Youtube.config import Config

# Create a Pyrogram client
app = Client(
    "my_bot",
    api_id=6831200, 
    api_hash=qTDCZhEmGkoHcm84_fbG20F3fHmHEcXStZXpO2eUpMk, 
    bot_token=7804594320:AAH5rho1160LZD67EaIw_dMT4zSlu9f-3A0,
    plugins=dict(root="Youtube")
)



# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
