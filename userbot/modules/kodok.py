# Yang Hapus Besok Mati Aminnn
# Port By @Vckyouuu

from telethon.errors import ChatSendInlineForbiddenError, ChatSendStickersForbiddenError

from userbot.events import register
from userbot import CMD_HELP, bot


@register(outgoing=True, pattern=r"^\.prog (.*)")
async def honkasays(event):
    await event.edit("`Sedang Memprosess!!!`")
    text = event.pattern_match.group(1)
    if not text:
        return await event.edit("`Masukin text dulu, Contoh .prog owner jelek`")
    try:
        if not text.endswith("."):
            text = text + "."
        if len(text) <= 9:
            results = await bot.inline_query("honka_says_bot", text)
            await results[2].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        elif len(text) >= 14:
            results = await bot.inline_query("honka_says_bot", text)
            await results[0].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        else:
            results = await bot.inline_query("honka_says_bot", text)
            await results[1].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        await event.delete()
    except ChatSendInlineForbiddenError:
        await event.edit("`Ga bisa ngirim pesan inline disini.`")
    except ChatSendStickersForbiddenError:
        await event.edit("Ga ada izin untuk mengirimkan stiker disini!")


CMD_HELP.update({"prog": "`.prog`\
    \nPenjelasan: .prog <kata kata>. Biar bisa lihat kodok bentuk badut"})
