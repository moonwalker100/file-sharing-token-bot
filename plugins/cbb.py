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
            text = """<b>🤖 ᴍʏ ɴᴀᴍᴇ: {botname}

<b><blockquote expandable>» ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/Here_remo>Ꮢᴇᴍᴏ 🜲</a>
» ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href=https://t.me/play_tamil_dubbed_series>ᴘʟᴀʏ ᴄᴏᴍᴍᴜɴɪᴛʏ</a>
» ᴀᴅᴠᴀɴᴄᴇ ғᴇᴀᴛᴜʀᴇs: <a href=https://telegra.ph/BOT-FEATURES-11-09-28>Cʟɪᴄᴋ ʜᴇʀᴇ</a>
» ʟᴀɴɢᴜᴀɢᴇ: <a href=https://docs.python.org/3/>Pʏᴛʜᴏɴ 3</a>
» ʟɪʙʀᴀʀʏ: <a href=https://docs.pyrogram.org/>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>
» ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/Here_remo>Ꮢᴇᴍᴏ</a></blockquote></b>"""
            
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
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
