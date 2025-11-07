from telethon import TelegramClient, events
import os
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
ABH = TelegramClient("ABH_session", api_id, api_hash)
async def main():
    await ABH.start(bot_token=bot_token)
    print("✅ Bot is running and connected successfully.")
    await ABH.run_until_disconnected()
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
