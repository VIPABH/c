from telethon import events, Button
from Resources import *
from ABH import *
devrs = [1910015590, 1418998675]
print('i am live')
b = [Button.inline('اضافة مراقب', data="addwatcher"), Button.inline('اضافة ناشر', data='addpostman')]
@ABH.on(events.NewMessage(pattern='/start'))
async def start(e):
    id = e.sender_id
    if not id in devrs:
        await e.reply('🙂')
        return
    await e.reply(f'اهلا عزيزي ( {await mention(e)} ) شنو تحب تسوي اليوم؟', buttons=b)
@ABH.on(events.CallbackQuery)
async def adds(e):
    data = e.data.decode('utf-8')
    user_id = e.sender_id
    if data in ("addwatcher", "addpostman"):
        await e.edit(" أرسل الآن آيدي المستخدم لإضافته.")
        async def get_user_id(event):
            if event.sender_id != user_id:
                return
            uid = event.raw_text.strip()
            if not uid.isdigit():
                await event.reply(" صيغة غير صحيحة، أرسل رقم الآيدي فقط.")
                return
            if data == "addwatcher":
                await event.reply(f"👁️ تم إضافة المراقب بالآيدي `{uid}` بنجاح.")
            elif data == "addpostman":
                await event.reply(f"📨 تم إضافة الناشر بالآيدي `{uid}` بنجاح.")
            ABH.remove_event_handler(get_user_id, events.NewMessage)
        ABH.add_event_handler(get_user_id, events.NewMessage)
