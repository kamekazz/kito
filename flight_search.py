import requests
from flight_schema import FlightSchema
from dotenv import load_dotenv
import os
load_dotenv()

TEQUILA_ENDPOINT = os.getenv('TEQUILA_ENDPOINT')
TEQUILA_API_KEY = os.getenv('TEQUILA_API_KEY')


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint,
                                headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, fly_from, fly_to, date_from, date_to, nights):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            # "date_from": from_time.strftime("%d/%m/%Y"),
            # "date_to": to_time.strftime("%d/%m/%Y"),

            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": nights,
            "nights_in_dst_to": nights,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {date_to}.")
            return None

        flight_data = FlightSchema(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
            buy_url=data["deep_link"]
        )
        print(
            f"{flight_data.destination_city}: ${flight_data.price} \n  sale el dia :{flight_data.out_date} y vuelve el dia:{flight_data.return_date} \n Para compra:{flight_data.buy_url}")
        return flight_data
