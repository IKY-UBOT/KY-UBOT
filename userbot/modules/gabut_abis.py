from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
# Create by myself @uurfavboys


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi Seleb Mau Nimbrung Kaka..**")


@register(outgoing=True, pattern='^.bf(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Kyura pembokep handal☑️**")
    await typew.edit("**Kyura pembokep handal✅**")
    sleep(3)
    await typew.edit("**Ken kan kang suges☑️**")
    await typew.edit("**Ken kan kang suges✅**")
    sleep(3)
    await typew.edit("**Kyy si paling galau☑️**")
    await typew.edit("**Kyy si paling galau✅**")
    sleep(3)
    await typew.edit("**Skyzu lord cgban☑️**")
    await typew.edit("**Skyzu lord cgban✅**")
    sleep(3)
    await typew.edit("**Ari bandar pekob☑️**")
    await typew.edit("**Ari bandar pekob✅**")
    sleep(3)
    await typew.edit("**Alfha si paling fake os☑️**")
    await typew.edit("**Alfha si paling fake os✅**")
    sleep(3)
    await typew.edit("**Zaen jamet abis☑️**")
    await typew.edit("**Zaen jamet abis✅**")
    sleep(3)
    await typew.edit("**TD manusia gunung☑️**")
    await typew.edit("**TD manusia gunung✅**")
    sleep(3)
    await typew.edit("**FATUR PALING GANTENG!**")

@register(outgoing=True, pattern='^.pbl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`PP bule?`")
    sleep(2)
    await typew.edit("`ANJINK...ada PP bule`")
    sleep(2)
    await typew.edit("`BABI!!!`")
    sleep(3)
    await typew.edit("`Udah PP bule PINTEREST lagi, goblok!!!`")
    sleep(3)
    await typew.edit("`Kalo ga punya muka minimal modal lah BANGSAT...Dasar bocah pinterest`")


@register(outgoing=True, pattern='^.lahk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Lahk, Lu Goblok Apa Tolol?`")
    sleep(3)
    await typew.edit("`Apa Autis?`")
    sleep(2)
    await typew.edit("`Gosah sokeras lu kontolll`")
    sleep(2)
    await typew.edit("`Gua ga takut sama bocah bocah ampas kek lu kontollll!`")


@register(outgoing=True, pattern='^.war(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wah, Ada war gais...`")
    sleep(2)
    await typew.edit("`Tapi, kalo diliat-liat kesannya lebih ke stand up komedi😅`")
    sleep(3)
    await typew.edit("`ehh iya, Lu kan badut🤡`")
    sleep(3)
    await typew.edit("`Disuruh war malah cerpen`")
    sleep(3)
    await typew.edit("`kebanyakan baca dongeng ya gini.`")
    sleep(3)
    await typew.edit("`Keras kaga dongo iya,kek badut ulang tahun yg kaga di gaji`")
    sleep(3)
    await typew.edit("`Bocah goblok yang goblok goblok banget seperti rucika mengalir sampai jauh, Lu lebih goblok lagi goblok gobloknya keturunan sampai lu lahir!`")

CMD_HELP.update({
    "Gabut":
    "`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.bf` ; `.war` ; `.lahk` ; `.pbl`\
    \nUsage: liat aza."
})
