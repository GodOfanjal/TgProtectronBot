from telethon import events, Button
from TgProtectronBot import Stark
from Configs import Config

btn =[
    [Button.inline("Aᴅᴍɪɴ", data="admin"), Button.inline("Bᴀɴs", data="bans")],
    [Button.inline("Pɪɴs", data="pins"), Button.inline("Pᴜʀɢᴇ", data="purges")],
    [Button.inline("Lᴏᴄᴋs", data="locks"), Button.inline("Iɴғᴏ", data="info")],
    [Button.inline("Cʟᴇᴀɴᴇʀ", data="zombies")]]

HELP_TEXT = """
**Hi i am {} help menu here**

/start - To Start Me ;)
/help - To Get Available Help Menu

""".format(Config.BOT_USERNAME)


@Stark.on(events.NewMessage(pattern="[!?/]help"))
async def help(event):

    if event.is_group:
       await event.reply("Contact me in PM to get available help menu!", buttons=[
       [Button.url("Help And Commands!", "T.me/{}?start=help".format(Config.BOT_US))]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@Stark.on(events.NewMessage(pattern="^/start help"))
async def _(event):

    await event.reply(HELP_TEXT, buttons=btn)

@Stark.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):

     await event.edit(HELP_TEXT, buttons=btn)
