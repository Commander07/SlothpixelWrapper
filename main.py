import requests
baseurl = "https://api.slothpixel.me/api/"

class api:

    def __init__(self, apikey=None):
        self.apikey = apikey
        self.players = self.players(apikey=self.apikey)

    class players:

        def __init__(self, apikey=None):
            self.apikey = apikey

        def get(self, ign):
            return requests.get(url=f"{baseurl}players/{ign}{'?key='+self.apikey if self.apikey is not None else ''}").json()

        def achievements(self, ign):
            return requests.get(url=f"{baseurl}players/{ign}/achievements{'?key='+self.apikey if self.apikey is not None else ''}").json()

        def quests(self, ign):
            return requests.get(url=f"{baseurl}players/{ign}/quests{'?key='+self.apikey if self.apikey is not None else ''}").json()

        def recentGames(self, ign):
            return requests.get(url=f"{baseurl}players/{ign}/recentGames{'?key='+self.apikey if self.apikey is not None else ''}").json()

        def friends(self, ign):
            return requests.get(url=f"{baseurl}players/{ign}/friends{'?key='+self.apikey if self.apikey is not None else ''}").json()

        def status(self, ign):
            return requests.get(url=f"{baseurl}players/{ign}/status{'?key='+self.apikey if self.apikey is not None else ''}").json()

    class guild:

        def __init__(self, apikey=None):
            self.apikey = apikey

        def get(self, ign: str, populatePlayers=None):
            return requests.get(url=f"{baseurl}guilds/{ign}{'?key='+self.apikey if self.apikey is not None else ''}").json()

        def name(self, name: str, populatePlayers=None):
            return requests.get(url=f"{baseurl}guilds/name/{name}{'?key='+self.apikey if self.apikey is not None else ''}").json()

        def id(self, id: str, populatePlayers=None):
            return requests.get(url=f"{baseurl}guilds/id/{id}{'?key='+self.apikey if self.apikey is not None else ''}").json()

slothpixel = api()