from userbot import CMD_HELP, bot
from userbot import CMD_HANDLER as cmd
from userbot.utils import dior_cmd


@dior_cmd(pattern="xogame(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()


@dior_cmd(pattern="whisp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()


@dior_cmd(pattern="mod(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    modr = event.pattern_match.group(1)
    botusername = "@PremiumAppBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, modr)
    await tap[0].click(event.chat_id)
    await event.delete()

CMD_HELP.update({
    "games": "\
πΎπ€π’π’ππ£π: `{cmd}xogame`\
\nβ³ : Mainkan game XO bersama temanmu.\
\n\nπΎπ€π’π’ππ£π: `{cmd}mod <nama app>`\
\nβ³ : Dapatkan applikasi mod\
\n\nπΎπ€π’π’ππ£π: `{cmd}whisp <teks> <username>`\
\nβ³ : Berikan pesan rahasia"})
