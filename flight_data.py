import requests
from datetime import datetime, timedelta

class FlightData:
    def __init__(self):
        self.apikey = "Your API Key"
        self.get_endpoint = "Your endpoint"
        self.departure_airport = "Provide IATA Code of your airport"
        self.tomorrow = datetime.now() + timedelta(1)
        self.next_6_month = datetime.now() + timedelta(30*6)
        self.currency = "USD"
        self.night_in_from = 6
        self.night_in_to = 27
        self.stop_overs = 0

    def find_flight(self, sheet):

        header = {
            "apikey": self.apikey
        }

        result = []
        for row in sheet:
            config = {
            "fly_from": self.departure_airport,
            "fly_to": row["iataCode"],
            "date_from": self.tomorrow.strftime("%d/%m/%Y"),
            "date_to": self.next_6_month.strftime("%d/%m/%Y"),
            "nights_in_dst_from": self.night_in_from,
            "nights_in_dst_to": self.night_in_to,
            "flight_type": "round",
            "curr": self.currency,
            "max_stopovers": self.stop_overs,
            }
            
            response = requests.get(url=self.get_endpoint, params=config, headers=header)
            try:
                data = response.json()["data"][0]
            except IndexError:
                return result
            # if row["lowestPrice"] > data["price"]:
            stop_over_list = [stop_over["cityFrom"] for stop_over in data["route"] if stop_over["cityFrom"] != data["cityTo"] and stop_over["cityFrom"] != data["cityFrom"]]
            stop_over_list = list(set(stop_over_list))
            result.append({
                "Price": data["price"],
                "Departure City": data["cityFrom"],
                "Departure IATA": data["flyFrom"],
                "Arrival City": data["cityTo"],
                "Arrival IATA": data["flyTo"],
                "Departure Time": str(self.tomorrow + timedelta(minutes=data["duration"]["departure"])).split()[0],
                "Return Time": str(self.tomorrow + timedelta(minutes=data["duration"]["departure"]) + timedelta(days=data["nightsInDest"])).split()[0],
                "Stop Overs": stop_over_list
            })
        
        return result