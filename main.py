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
            return requests.get(url=f"{baseurl}players/{ign}/achievements").json()

        def quests(self, ign):
            return requests.get(url=f"{baseurl}players/{ign}/quests").json()

        def recentGames(self, ign):
            return requests.get(url=f"{baseurl}players/{ign}/recentGames").json()

        def friends(self, ign):
            return requests.get(url=f"{baseurl}players/{ign}/friends").json()

        def status(self, ign):
            return requests.get(url=f"{baseurl}players/{ign}/status").json()

slothpixel = api()