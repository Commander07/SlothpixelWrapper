import requests
baseurl = "https://api.slothpixel.me/api/"


class API:

    def __init__(self, apikey=None):
        self.apikey = apikey
        self.players = self.players(apikey=self.apikey)
        self.guilds = self.guilds(apikey=self.apikey)
        self.skyblock = self.skyblock(apikey=self.apikey)
        self.leaderboards = self.leaderboards(apikey=self.apikey)
        self.boosters = self.boosters(apikey=self.apikey)
        self.bans = self.bans(apikey=self.apikey)
        self.counts = self.counts(apikey=apikey)

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

    class guilds:

        def __init__(self, apikey=None):
            self.apikey = apikey

        def get(self, ign: str, populatePlayers=None):
            url = f"{baseurl}guilds/{ign}{'?key='+self.apikey if self.apikey is not None else ''}"
            url += ("&populatePlayers=1" if "?key=" in url else "?populatePlayers=1") if populatePlayers is not None else ""
            return requests.get(url=url).json()

        def name(self, name: str, populatePlayers=None):
            url = f"{baseurl}guilds/name/{name}{'?key='+self.apikey if self.apikey is not None else ''}"
            url += ("&populatePlayers=1" if "?key=" in url else "?populatePlayers=1") if populatePlayers is not None else ""
            return requests.get(url=url).json()

        def id(self, id: str, populatePlayers=None):
            url = f"{baseurl}guilds/id/{id}{'?key='+self.apikey if self.apikey is not None else ''}"
            url += ("&populatePlayers=1" if "?key=" in url else "?populatePlayers=1") if populatePlayers is not None else ""
            return requests.get(url=url).json()

    class skyblock:

        def __init__(self, apikey=None):
            self.apikey = apikey
            self.auctions = self.auctions(apikey=apikey)

        def profiles(self, ign):
            return

        def profile(self, ign, profileId=None):
            return

        def items(self):
            return

        def bazaar(self, itemId):
            return

        class auctions:

            def __init__(self, apikey=None):
                self.apikey = apikey

            def get(self, sortBy, limit=100, active=True, sortOrder="desc", page=None, auctionUUID=None, itemUUID=None, id=None):
                return

            def past(self, itemId, from_=None, to=None, showAuctions=None):
                return

    class leaderboards:

        def __init__(self, apikey=None):
            self.apikey = apikey

        def get(self, type, columns, sortBy, sortOrder="desc", limit=None, page=None, significant=True):
            return

        def template(self, template):
            return

    class boosters:

        def __init__(self, apikey=None):
            self.apikey = apikey

        def get(self):
            return

        def game(self, game):
            return

    class bans:

        def __init__(self, apikey=None):
            self.apikey = apikey

        def get(self):
            return

    class counts:

        def __init__(self, apikey=None):
            self.apikey = apikey

        def get(self):
            return


slothpixel = API()
