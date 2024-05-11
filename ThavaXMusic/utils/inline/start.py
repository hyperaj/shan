from pyrogram.types import InlineKeyboardButton

import config
from ThavaXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀𝐝𝐝 𝐦𝐞 𝐝𝐞𝐚𝐫 🫣",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="𝐇𝐞𝐥𝐩", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="𝐍𝐞𝐭𝐰𝐨𝐫𝐤", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="𝐃𝐚𝐫𝐥𝐢𝐧𝐠 ᥫ᭡", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="𝐁𝐨𝐲 𝐁𝐞𝐬𝐭𝐢𝐞", url=f"https://t.me/Idhayann"),
        ],
    ]
    return buttons
