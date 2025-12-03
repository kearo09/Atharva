# welcome = [
#     "**{tag}** madhar chod ",
#     "**{tag}** bhenchod",
#     " **{tag}** kutte rand ke bacche",
#     " **{tag}** 4 burj khalifa teri ma ke ghusa",
#     " **{tag}** tab tu paida hua rand ka baccha",
#     "**{tag}** randi ki aulad",
#     "**{tag}** teri ma public washroom hai",
#     "**{tag}** har koi mut deta","bsdk tera baap sala na mard tha",
#     "**{tag}** teri ma ko chodne aana pada tha mereko .",
#     " **{tag}** tera baap osama bin laden ka nazayas aaulad tha",
#     "**{tag}** teri ma ki gand me bomb dalkar ched banata tha",
#     "**{tag}** teri ma ki gand me muth marunga","mut dunga",
#     "**{tag}** randi banakr chodunga","chut cheer faad kardunga",
#     "**{tag}** wo roz mera lund lene aaygi",
#     "**{tag}** baap se bakchodi mat kar ladle",
#     "**{tag}** janta nahi hai chut fad kar chaba jaunga",
#     "**{tag}** teri maiya ke bhur me biology ki book daldunga",
#     "**{tag}** teri ma ka bhosada bhari sabha me pradan karwaunga",
#     "**{tag}** khatam hogai hai daru khatam hogai hai chakna teri ma chodne aara salwar khole kar rakhna",
#     "**{tag}** loduchudu",
#     "**{tag}** tereko kale ghode ka lauda chusaunga",
#     "**{tag}** teri jindagi jhand hai leta mera lund hai",
#     "**{tag}** chuda chuda kar tu rand hogai haveli se badi teri gand hogai",
#     "**{tag}** Khatam ho gayi chatni khatam ho gaya chakna aa raha hoo madarchod tu apni maa ki salwar khol pussy taiyar rakhna"
# ]



import asyncio
from telethon import TelegramClient, events

API_ID = 35324544
API_HASH = "76a2b357dc79c430948bbe6781495616"
SESSION = "bakaSession"

client = TelegramClient(SESSION, API_ID, API_HASH)

running = False
target_user_id = None
OWNER_ID = None  

welcome = [
    "**{tag}** madhar chod ",
    "**{tag}** bhenchod",
    " **{tag}** kutte rand ke bacche",
    " **{tag}** 4 burj khalifa teri ma ke ghusa",
    " **{tag}** tab tu paida hua rand ka baccha",
    "**{tag}** randi ki aulad",
    "**{tag}** teri ma public washroom hai",
    "**{tag}** har koi mut deta","bsdk tera baap sala na mard tha",
    "**{tag}** teri ma ko chodne aana pada tha mereko .",
    " **{tag}** tera baap osama bin laden ka nazayas aaulad tha",
    "**{tag}** teri ma ki gand me bomb dalkar ched banata tha",
    "**{tag}** teri ma ki gand me muth marunga","mut dunga",
    "**{tag}** randi banakr chodunga","chut cheer faad kardunga",
    "**{tag}** wo roz mera lund lene aaygi",
    "**{tag}** baap se bakchodi mat kar ladle",
    "**{tag}** janta nahi hai chut fad kar chaba jaunga",
    "**{tag}** teri maiya ke bhur me biology ki book daldunga",
    "**{tag}** teri ma ka bhosada bhari sabha me pradan karwaunga",
    "**{tag}** khatam hogai hai daru khatam hogai hai chakna teri ma chodne aara salwar khole kar rakhna",
    "**{tag}** loduchudu",
    "**{tag}** tereko kale ghode ka lauda chusaunga",
    "**{tag}** teri jindagi jhand hai leta mera lund hai",
    "**{tag}** chuda chuda kar tu rand hogai haveli se badi teri gand hogai",
    "**{tag}** Khatam ho gayi chatni khatam ho gaya chakna aa raha hoo madarchod tu apni maa ki salwar khol pussy taiyar rakhna"
]

async def is_owner(event):
    global OWNER_ID
    if OWNER_ID is None:
        me = await client.get_me()
        OWNER_ID = me.id
    return event.sender_id == OWNER_ID

@client.on(events.NewMessage(pattern=r"^\.start$"))
async def start_cmd(event):
    global running, target_user_id

    if not await is_owner(event):
        return await event.reply("❌ Only owner can use `.start`.")

    # Must reply to user
    if not event.is_reply:
        return await event.reply("Reply to a user and then use `.start`.")

    replied = await event.get_reply_message()
    victim = await replied.get_sender()

    if not victim:
        return await event.reply("User fetch error.")

    tag = f"[{victim.first_name}](tg://user?id={victim.id})"
    target_user_id = victim.id
    running = True

    await event.reply(
        f"🔥 Started welcome loop on {tag}\nUse `.stop` to stop.",
        parse_mode="md"
    )

    delay = 0.8

    while running:
        for line in welcome:
            if not running:
                break

            msg = line.format(tag=tag)
            await client.send_message(event.chat_id, msg, parse_mode="md")
            await asyncio.sleep(delay)
            
@client.on(events.NewMessage(pattern=r"^\.stop$"))
async def stop_cmd(event):
    global running

    if not await is_owner(event):
        return await event.reply("❌ Only owner can use `.stop`.")

    if running:
        running = False
        await event.reply("⛔ Flood Stopped.")
    else:
        await event.reply("Flood is not running.")


print("🔥 Userbot Running…")
client.start()
client.run_until_disconnected()
