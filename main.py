# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
import time
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

# ORIGIN_CITY_IATA = "EWR"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# tomorrow = datetime.now() + timedelta(days=1)
# six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# for destination in sheet_data:
#     flight = flight_search.check_flights(
#         ORIGIN_CITY_IATA,
#         destination["iataCode"],
#         from_time=tomorrow,
#         to_time=six_month_from_today
#     )

print('Hola kendra desde donde queires viajar?')
ui_form = input()
print(f"OK NEWARK AIRPORT")
time.sleep(2)
print('Que bien')
time.sleep(1)
ui_to = input('para donde queres viajar?')
ui_date_from = input('desde que dia quires comesa a buscar?')
ui_date_to = input('cual es la nutima feche que puedes vijar?')
ui_nights_in_dst_ = int(input('cuantos diaS queres pasar?'))
ui_like_price = input('cuanto queres pagar?')


flight = flight_search.check_flights(
    fly_from=ui_form.upper(),
    fly_to=ui_to.upper(),
    date_from=ui_date_from,
    date_to=ui_date_to,
    nights=ui_nights_in_dst_
)
