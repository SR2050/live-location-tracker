from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from colorama import Fore, Back, Style

text = f'''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠻⠟⠿⢿⠿⠟⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⡟⠟⠃⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⡟⠛⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠠⠁⠀⠂⠀⠀⠺⣷⣶⣄⠀⠀⠀⠀⠀⢀⣸⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⡿⢉⣭⡶⢿⡟⠛⠉⠉⠀⠈⠹⠿⢿⣿⡍⠩⣭⣿⣿⣿⣿⣿⣿⣿
⡿⠛⠁⠉⠙⠛⠛⠉⠀⠀⠀⠀⠀⠀⠂⢀⣄⠈⠿⣿⡄⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⠛⠉⠉⠛⠿⠿⠓⠈⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠙⠃⠿⣿
⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣬⠀⠀⣠⣾⣧⠀⢠⣾⣿⣧⣤⣾⣿⣿⡟⠁⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⣦⣾
⣿⣇⣠⣴⣿⣷⣦⠀⠀⠀⠀⠀⠀⠈⠙⢻⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⠃⠹⡧⠀⠐⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣶⡎⢀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⣙⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢨⣿⣷⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠶⠀⢀⡀⡈⠁⠁⠀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⣠⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⣀⣀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠈⠙⠉⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠛⢩⣤⣉⣛⢿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣦⠀⠀⣀⡄⠀⠀⢀⣴⡖⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣘⠛⠙⠛⠻⢿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣧⠘⣿⣷⠆⢄⣸⡿⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠛⠿⢿⣿⣿⣿⣿⣿⣿⣷⡂⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⠋⠀⠈⡍⠙⠛⢿⡿⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠈⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣽⣤⠹⠛⢣⠠⣴⣦⣽⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⣶⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠁⠀⠀⠀⠀⠹⣿⣏⣻⣿⣶⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⣀⣀⠀⠀⠀⣸⣿⣿⡿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⢀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⢸⣿⣿⡿⠃⣨⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣼⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
'''

print(Back.BLACK+Fore.WHITE+text)
print(Fore.RED+"Author:"+Fore.LIGHTGREEN_EX+"Shiboshree Roy\n"+Fore.LIGHTYELLOW_EX+"Programm:"+Fore.LIGHTCYAN_EX+"Location Tracker\n"+Fore.WHITE+"Version :"+Fore.RED+"1.2.0")
print("\n")

def get_location():
    geolocator = Nominatim(user_agent="location_tracker")
    while True:
        try:
            address = input(Fore.YELLOW+"Enter an address or location : ")
            location =geolocator.geocode(address)
            break
        except GeocoderTimedOut:
            print(Fore.GREEN+"Geocoding service timeout. retrying....")
    if location is not None:
        print(Fore.WHITE+"latitude :",location.latitude)
        print(Fore.RED+"longitude :",location.longitude)
        print(Fore.BLUE+"Address :",location.address)
    else:
        print(Fore.RED+"Location not found..")
get_location()