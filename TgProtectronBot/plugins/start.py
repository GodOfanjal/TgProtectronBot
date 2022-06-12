from TgProtectronBot import Stark
from telethon import events, Button

PM_START_TEXT = """
**Hi {}**
I am simple manager bot whos help to you for manage your group

**Click the below help button for the open help menu!**
"""

@Stark.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.reply(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.inline("Help & Commands", data="help")],
        [Button.url("Add Me To Your Group", "https://t.me/{BOT_USERNAME}?startgroup=true")]])
       return

    if event.is_group:
       await event.reply("**I AM ALIVE ✨**")
       return
