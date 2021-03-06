from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""π Hi {message.from_user.first_name}!
β¨ I am Jaadu Music Player. π
π₯³ I can play music in your Telegram Group's Voice Chatπ
βοΈ Use these buttons below to know more. π""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β Source code", url="https://github.com/Amberyt/Jaadu-Music-Bot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π¬ Group", url="t.me/Jaadubotofficial"
                    ),
                    InlineKeyboardButton(
                        "Channel π", url="https://t.me/jaadubotofficial"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "β Close β", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        "** JaaduOP:** I'm Working!!!\nUse me in Inline to search for a YouTube Video/Music. \n**Happy Streaming**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "πΆ Search πΆ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "β Close β", callback_data="close"
                    )
                ]
            ]
        )
    )
