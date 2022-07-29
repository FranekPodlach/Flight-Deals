from twilio.rest import Client

class NotificationManager:
    def __init__(self, data):
        self.sid = "Your SID"
        self.token = "Your Token"
        self.data = data

    def print_stop_overs(self, list):
        string = ""
        for city in list:
            string += f'{list[city]}, '
        return string

    def send_message(self):
        for dict in self.data:
            if dict["Stop Overs"] == []:
                client = Client(self.sid, self.token)
                message = client.messages \
                .create(
                    body = f'Low price allert! Only ${dict["Price"]} to fly from {dict["Departure City"]}-{dict["Departure IATA"]} to {dict["Arrival City"]}-{dict["Arrival IATA"]}, from {dict["Departure Time"]} to {dict["Return Time"]}, this is link to your flight: https://www.google.co.uk/flights?hl=en#flt={dict["Departure IATA"]}.{dict["Arrival IATA"]}.{dict["Departure Time"]}*{dict["Arrival IATA"]}.{dict["Departure IATA"]}.{dict["Return Time"]}',
                    from_ = "Your Number",
                    to = "Your Number",
                )    
                print(message.status)
            elif len(dict["Stop Overs"]) == 1:
                client = Client(self.sid, self.token)
                message = client.messages \
                .create(
                    body = f'Low price allert! Only ${dict["Price"]} to fly from {dict["Departure City"]}-{dict["Departure IATA"]} to {dict["Arrival City"]}-{dict["Arrival IATA"]}, from {dict["Departure Time"]} to {dict["Return Time"]} with 1 stop over in {dict["Stop Overs"][0]}, this is link to your flight: https://www.google.co.uk/flights?hl=en#flt={dict["Departure IATA"]}.{dict["Arrival IATA"]}.{dict["Departure Time"]}*{dict["Arrival IATA"]}.{dict["Departure IATA"]}.{dict["Return Time"]}',
                    from_ = "Your Number",
                    to = "Your Number",
                )    
                print(message.status)
            else:
                client = Client(self.sid, self.token)
                message = client.messages \
                .create(
                    body = f'Low price allert! Only ${dict["Price"]} to fly from {dict["Departure City"]}-{dict["Departure IATA"]} to {dict["Arrival City"]}-{dict["Arrival IATA"]}, from {dict["Departure Time"]} to {dict["Return Time"]} with {len(dict["Stop Overs"])} stop overs in {self.print_stop_overs(dict["Stop Overs"])}, this is link to your flight: https://www.google.co.uk/flights?hl=en#flt={dict["Departure IATA"]}.{dict["Arrival IATA"]}.{dict["Departure Time"]}*{dict["Arrival IATA"]}.{dict["Departure IATA"]}.{dict["Return Time"]}',
                    from_ = "Your Number",
                    to = "Your Number",
                )    
                print(message.status)

            