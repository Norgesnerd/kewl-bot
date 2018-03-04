import aiohttp, asyncio, io, discord
from discord.ext import commands
from discord.ext.commands import Bot

loop = asyncio.get_event_loop()
session = aiohttp.ClientSession(loop)

async with session as s:
    async with s.get('https://random.dog/woof.json') as resp:
        if resp.status == 200:
            dog_url = await resp.json()
            async with s.get(dog_url['url']) as dog:
                if dog.status == 200:
                    # We now have an image, but most libraries will require that we have a bytes like object so let's make one
                    dog_bytes = io.BytesIO(await dog.read())
                    # Now we can use dog_bytes like the following in discord.py
                    await some_channel_object_we_have.send(file=discord.File(dog_image, "random_dog.png"))