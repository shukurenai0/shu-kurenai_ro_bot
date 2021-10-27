from telethon import events, Button, custom
import re, os
from mrjoker.events import register
from mrjoker import telethn as tbot
from mrjoker import telethn as tgbot
PHOTO = "https://telegra.ph/file/c51b8dafd99ddf0bd30a6.jpg"
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**🐺 I,m Wolf X** \n\n"
  PIKACHU += "**🐺 I'm Working Properly**\n\n"
  PIKACHU += "**🐺 Wolf X : 2.0 LATEST**\n\n"
  PIKACHU += "**🐺 My Master :** [Hacker](t.me/HMF_OWNER_1)\n\n"
  PIKACHU += "**🐺 Telethon Version : 1.23.0**\n\n"
  BUTTON = [[Button.url("𝙎𝙐𝙋𝙋𝙊𝙍𝙏", "https://t.me/wolfxbotz"), Button.url("Copyrights©️", "https://t.me/HMF_OWNER_1")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)
