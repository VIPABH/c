from ABH import *
from code import *
async def main():
    await ABH.start(bot_token=os.getenv("BOT_TOKEN"))
    await ABH.run_until_disconnected()
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
