# set multi cmd

from userbot import CMD_HELP
from userbot import CMD_HANDLER as cmd
from userbot.utils import dior_cmd

@dior_cmd(pattern="dm$")
async def remoteaccess(event):

    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:
        chat_id = int(chat_id)
    except BaseException:

        pass

    msg = ""
    mssg = await event.get_reply_message()
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("⚜️**Successfully sent your message**⚜️")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("⚜️**Successfully sent your message**⚜️")
    except BaseException:
        await event.edit("**Terjadi Error. Lu limit kayanya nyet.**")

CMD_HELP.update(
    {
        "message": "`{cmd}dm`\
    \nMengirim Pesan Dengan Jarak Jauh Dengan .dm <username> <pesan>."
    })
