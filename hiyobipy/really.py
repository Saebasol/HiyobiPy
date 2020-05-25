import aiohttp
from .fk import Response

class Async():

    async def apiindex(self):
        URL = 'https://api.hiyobi.me/notice'
        async with aiohttp.ClientSession() as cs:
            async with cs.get(URL) as r:
                response = await r.json()
                return Response(response)

    async def apigallery(self, index: int):
        URL = f'https://api.hiyobi.me/gallery/{index}'
        async with aiohttp.ClientSession() as cs:
            async with cs.get(URL) as r:
                response = await r.json()
                return Response(response)

    async def apisearch(self, search: list, page: int = 1):
        URL = f'https://api.hiyobi.me/search'
        data = {"search": search, "paging": page}
        async with aiohttp.ClientSession() as cs:
            async with cs.post(URL, json=data) as r:
                response = await r.json()
                return Response(response)

    async def apilist(self, page: int = 1):
        URL = f'https://api.hiyobi.me/list/{page}'
        async with aiohttp.ClientSession() as cs:
            async with cs.get(URL) as r:
                response = await r.json()
                return Response(response)

    async def cdnlist(self, index: int):
        URL = f'https://cdn.hiyobi.me/data/json/{index}_list.json'
        async with aiohttp.ClientSession() as cs:
            async with cs.get(URL) as r:
                response = await r.json()
                return Response(response)

    async def cdndownload(self, index: int, filename: str):
        URL = f'https://cdn.hiyobi.me/data/{index}/{filename}'
        async with aiohttp.ClientSession() as cs:
            async with cs.get(URL) as r:
                return r

    async def cdnthumbnail(self, index: int):
        URL = f'https://cdn.hiyobi.me/tn/{index}'
        async with aiohttp.ClientSession() as cs:
            async with cs.get(URL) as r:
                return r
