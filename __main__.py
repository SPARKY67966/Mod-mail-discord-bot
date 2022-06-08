import asyncio

from bot import ModMailBot
from discord import Intents


async def main():
    bot = ModMailBot(command_prefix='.', intents=Intents.all())
    async with bot:
        await bot.start()
        

asyncio.run(main())
