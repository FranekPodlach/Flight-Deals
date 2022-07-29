import requests

class DataManager:
    def __init__(self):
        self.get_endpoint = "Your endpoint"
        self.put_endpoint = "Your endpoint"
    
    def read_data(self):
        get_response = requests.get(url=self.get_endpoint)
        data = get_response.json()["prices"]
        return data
    
    def update_iata(self, new_sheet):
        for row in new_sheet:
            config = {
                "price": {
                    "iataCode": row["iataCode"],
                },
            }

            response = requests.put(url=self.put_endpoint + str(row["id"]), json=config)
