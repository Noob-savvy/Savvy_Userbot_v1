# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝒏𝒐𝒐𝒃 𝒔𝒂𝒗𝒗𝒚
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅

import sys
import datetime

from os import execle, environ
from config import ALIVE_PIC, SUDO_USERS

from pyrogram import Client, filters
from pyrogram.types import Message


DIVU = f"""☠︎︎𝐍𝐎𝐎𝐁_𝐒𝐀𝐕𝐕𝐘 ☠︎︎

➠ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.11.1`
➠ **ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ** : `1.4.16`
➠ **ʙᴏᴛ ᴠᴇʀsɪᴏɴ**  : `1.0`
➠ **ᴜᴘᴅᴀᴛᴇꜱ** : @Savvy_robot_update\n"""


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], ["/", ".", "!"]))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      Fuk = await e.reply("**Pong !!**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await Fuk.edit_text(f"◇ ☠︎︎𝐍𝐎𝐎𝐁_𝐒𝐀𝐕𝐕𝐘☠︎︎ \n◇ ᴘɪɴɢ: `{ms}ms`\n◇ ᴠᴇʀsɪᴏɴ: `3.3`")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], ["/", ".", "!"]))
async def alive(xspam: Client, msg: Message):
       if ".jpg" in ALIVE_PIC or ".png" in ALIVE_PIC:
              await xspam.send_photo(msg.chat.id, ALIVE_PIC, caption=DIVU)
       if ".mp4" in ALIVE_PIC or ".MP4," in ALIVE_PIC:
              await xspam.send_video(msg.chat.id, ALIVE_PIC, caption=DIVU)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["reboot", "restart"], ["/", ".", "!"]))
async def restart_bot(_, message: Message):
    msg = await message.reply("`ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
    args = [sys.executable, "main.py"]
    await msg.edit("» ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ...\n» ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ᴀғᴛᴇʀ 𝟷 ᴍɪɴᴜᴛᴇ ")
    execle(sys.executable, *args, environ)
