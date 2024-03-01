import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["مصنع","المصنع"])
    & filters.group
    & ~filters.edited
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1a3b073913ee104c8339b.jpg",
        caption=f"""مرحبا بك عزيزي في سورس ثريثون""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مصنع الميوزك", url=f"https://t.me/thirteenbbot"),
                    InlineKeyboardButton(
                        "المطور", url=f"https://t.me/TT_LLJ"),
                ],
                [
                   InlineKeyboardButton(
                        "𝐓𝐇𝐑𝐄𝐄 𝐓𝐇𝐔𝐍👑 ", url=f"https://t.me/CCYFC"),
                ],       
            ]
        ),
    )
    
    
    InlineKeyboardButton(
                        "𝐓𝐇𝐑𝐄𝐄 𝐓𝐇𝐔𝐍", url=f"https://t.me/CCYFC")
    
    
    
@app.on_message(
    command(["الكنيج"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("DEV_Eslam")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**¦𝙺𝙸𝙽𝙶 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )