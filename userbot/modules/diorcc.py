
from faker import Faker
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot import CMD_HANDLER as cmd
from userbot.utils import dior_cmd


@dior_cmd(pattern="gencc(?: |$)(.*)")
async def gencc(diorevent):
    if diorevent.fwd_from:
        return
    diorcc = Faker()
    diorname = diorcc.name()
    dioradre = diorcc.address()
    diorcard = diorcc.credit_card_full()

    await edit_or_reply(diorevent, f"__**👤 NAME :- **__\n`{diorname}`\n\n__**🏡 ADDRESS :- **__\n`{dioradre}`\n\n__**💸 CARD :- **__\n`{diorcard}`")


@dior_cmd(pattern="bin(?: |$)(.*)")
async def bin(event):
    if event.fwd_from:
        return
    geez_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1282429349))
            await event.client.send_message(chat, f"/bin {geez_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@dior_cmd(pattern="vbv(?: |$)(.*)")
async def vbv(event):
    if event.fwd_from:
        return
    dior_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1220829364))
            await event.client.send_message(chat, f"/vbv {dior_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@dior_cmd(pattern="key(?: |$)(.*)")
async def key(event):
    if event.fwd_from:
        return
    geez_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1282429349))
            await event.client.send_message(chat, f"/key {geez_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@dior_cmd(pattern="iban(?: |$)(.*)")
async def iban(event):
    if event.fwd_from:
        return
    geez_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1282429349))
            await event.client.send_message(chat, f"/iban {geez_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@dior_cmd(pattern="ccheck(?: |$)(.*)")
async def ccheck(event):
    if event.fwd_from:
        return
    geez_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1282429349))
            await event.client.send_message(chat, f"/ss {geez_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@dior_cmd(pattern="ccbin(?: |$)(.*)")
async def ccbin(event):
    if event.fwd_from:
        return
    geez_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit(f"Trying to generate CC from the given bin `{geez_input}`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1282429349))
            await event.client.send_message(chat, f"/gen {geez_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update({
    "ccarder": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}gencc`\
\n↳ : Generates Fake CC.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ccheck` <query>\
\n↳ : Checks That The Given CC is Live or Not.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}iban` <query>\
\n↳ : Checks That The Given IBAN ID is Live or Not.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}key` <query>\
\n↳ : Checks the status of probided key.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}vbv` <query>\
\n↳ : Checks the vbv status of given card.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}bin` <query>\
\n↳ : Checks that the given bin is valid or not.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ccbin` <bin>\
\n↳ : Generates CC from the given bin."
})
