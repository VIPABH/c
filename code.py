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
