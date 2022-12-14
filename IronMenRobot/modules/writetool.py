import requests
from requests import get
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from IronMenRobot import pbot as IronMen, BOT_NAME, BOT_USERNAME, SUPPORT_CHAT


@IronMen.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        text = message.text.split(None, 1)[1]
        m = await IronMen.send_message(
            message.chat.id, "`Please wait...,\n\nWriting your text...`"
        )
        API = f"https://api.sdbots.tk/write?text={text}"
        req = requests.get(API).url
        caption = f"""
Successfully Written Text ð

â¨ **Written By :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
ð¥ **Requested by :** {message.from_user.mention}
â **Link :** `{req}`
"""
        await m.delete()
        await IronMen.send_photo(
            message.chat.id,
            photo=req,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("â¢ á´á´Êá´É¢Êá´á´©Ê â¢", url=f"{req}")]]
            ),
        )
    else:
        lol = message.reply_to_message.text
        m = await IronMen.send_message(
            message.chat.id, "`Please wait...,\n\nWriting your text...`"
        )
        API = f"https://api.sdbots.tk/write?text={lol}"
        req = requests.get(API).url
        caption = f"""
Successfully Written Text ð

â¨ **Written By :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
ð¥ **Requested by :** {message.from_user.mention}
â **Link :** `{req}`
"""
        await m.delete()
        await IronMen.send_photo(
            message.chat.id,
            photo=req,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("â¢ á´á´Êá´É¢Êá´á´©Ê â¢", url=f"{req}")]]
            ),
        )


__mod_name__ = "WÊÉªá´á´Tá´á´Ê"

__help__ = """

 Writes the given text on white page with a pen ð

â /write <text> *:* Writes the given text.
 """
