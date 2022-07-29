from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.read_data()

if sheet_data[0]["iataCode"] == "":
    iata_codes = []
    for row in sheet_data:
        city = row["city"]
        row["iataCode"] = flight_search.find_iata(city)

    data_manager.update_iata(sheet_data)
    sheet_data = data_manager.read_data()
print("IATA codes updated")

flight_data = FlightData()
list_of_dict = []

list_of_dict = flight_data.find_flight(sheet_data)
if list_of_dict == []:
    while list_of_dict == []:
        flight_data.stop_overs += 1
        list_of_dict = flight_data.find_flight(sheet_data)     
print("Flights found")

notification_man = NotificationManager(list_of_dict)
notification_man.send_message()
print("Messages sent")
