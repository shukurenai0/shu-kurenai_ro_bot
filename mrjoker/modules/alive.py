from telethon import events, Button, custom
import re, os
from mrjoker.events import register
from mrjoker import telethn as tbot
from mrjoker import telethn as tgbot
PHOTO = "https://telegra.ph/file/c8ea5f5e21c09a0d2f5c9.jpg"
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**😎 I,𝖒 𝖘𝖍𝖚 𝖐𝖚𝖗𝖊𝖓𝖆** \n\n"
  PIKACHU += "**😎 I'm Working Properly**\n\n"
  PIKACHU += "**😎 𝖘𝖍𝖚-𝖐𝖚𝖗𝖊𝖓𝖆 : 2.0 LATEST**\n\n"
  PIKACHU += "** 😎 My Master :** [𝕯𝖊𝖊𝖕𝖆𝖐 𝖏𝖆𝖈𝖐](t.me/deepakjack007)\n\n"
  PIKACHU += "**Telethon Version : 1.23.0**\n\n"
  BUTTON = [[Button.url("𝙎𝙐𝙋𝙋𝙊𝙍𝙏", "https://t.me/shukurenairobot007"), Button.url("Copyrights©️", "https://t.me/deepakjack007")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)
