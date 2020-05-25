import requests
from .fk import Response


class Sync():

    def apiindex(self):
        URL = 'https://api.hiyobi.me/notice'
        r = requests.get(URL)
        return Response(r.json())

    def apigallery(self, index: int):
        URL = f'https://api.hiyobi.me/gallery/{index}'
        r = requests.get(URL)
        return Response(r.json())

    def apisearch(self, search: list, page: int = 1):
        URL = f'https://api.hiyobi.me/search'
        data = {"search": search, "paging": page}
        r = requests.post(URL, json=data)
        return Response(r.json())

    def apilist(self, page: int = 1):
        URL = f'https://api.hiyobi.me/list/{page}'
        r = requests.get(URL)
        return Response(r.json())

    def cdnlist(self, index: int):
        URL = f'https://cdn.hiyobi.me/data/json/{index}_list.json'
        r = requests.get(URL)
        return Response(r.json())

    def cdndownload(self, index: int, filename: str):
        URL = f'https://cdn.hiyobi.me/data/{index}/{filename}'
        r = requests.get(URL)
        return r

    def cdnthumbnail(self, index: int, filename: str):
        URL = f'https://cdn.hiyobi.me/tn/{index}'
        r = requests.get(URL)
        return r

