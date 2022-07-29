import requests

class FlightSearch:
    def __init__(self):
        self.get_endpoint = "Your endpoint"
        self.apikey = "Your API Key"

    def find_iata(self, city):
        config = {
            "term": city,
        }

        headers = {
            "apikey": self.apikey
        }

        response = requests.get(url=self.get_endpoint, headers=headers, params=config)
        data = response.json()
        return data["locations"][0]["code"]


