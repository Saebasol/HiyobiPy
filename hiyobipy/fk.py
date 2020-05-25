class Response:
    def __init__(self, response):
        self.data = response

    def __getattr__(self, attr):
        return self.data.get(attr)

    def __dict__(self):
        return self.data