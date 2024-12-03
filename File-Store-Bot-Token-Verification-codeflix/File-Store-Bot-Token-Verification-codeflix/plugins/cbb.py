#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>AURIGA</a>\n○ BOTS : <a href='https://t.me/supplywala_bots'>SUPPLYWALA BOTS</a>\n○ BACKUP : <a href='https://t.me/SUPPLYWALAH'>SUPPLYWALAH</a>\n○ SUPPORT : <a href='https://t.me/AURIGA_XD'>AURIGA_XD</a>\n○ CREATE YOUR OWN BOT : <a href='https://t.me/HACKING_FREAKS'>HACKING FREAKS</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/SUPPLYWALA_MEMBERSHIP')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
