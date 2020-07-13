import requests

class Scrapper:
    def __init__(self, path):
        self.key = self.read_api_key(path)
        self.api_url = 'https://{}.api.riotgames.com/val'
        self.api_match_url = self.api_url + '/match/v1/matches/{}}&api_key={}'
        self.api_match_list_url = self.api_url + '/match/v1/matchlists/by-puuid/{}&api_key={}'
        self.region = 'EU'
    
    def read_api_key(self, path: str) -> str:
        with open(path, 'r') as f:
            return f.read().strip()

    def request_match_list(self, puuid: str):
        print(self.api_match_list_url.format(self.region, puuid, self.key))
        print(requests.get(self.api_match_list_url.format(self.region, puuid, self.key)))
        return requests.get(self.api_match_list_url.format(self.region, puuid, self.key))

