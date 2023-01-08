############################HEADER################################
# Title: Weather Data
# Author: Anuj Tanwar
# Create Date: 06/04/2021
##################################################################

############################CHANGE LOG############################
# Change#:
# Change(s) Made:
# Date of Change:
# Author:   
# Change Approved by:
# Date Moved to Production:
##################################################################
import requests
import textwrap

from datetime import datetime
from termcolor import colored
from pprint import pprint

from pyzipcode import ZipCodeDatabase

# Function to test internet connection
def internet_on():
    try:
        requests.head("https://www.google.com", timeout=5)
    except requests.ConnectionError as err:
        print(colored("Internet is not working", 'red'))
        raise SystemExit(err)

# Function to fetch weather forecast using zip code
def weather_zip(api_key, zip_code, unit):
    try:
        r = requests.get("https://api.openweathermap.org/data/2.5/weather?zip=" + zip_code + "&appid=" + api_key + "&units=" + unit).json()
    except requests.exceptions.ConnectTimeout as ce:
        print("Connection timed out. Error message :: ", ce)
        raise SystemExit(ce)
    except requests.exceptions.HTTPError as he:
        if he.code == 404:
            print("Connection timed out. Error message :: ", he)
            raise SystemExit(he)
    except requests.ConnectionError as cone:
        print(colored("Connection is not working", 'red'))
        raise SystemExit(cone)
    except requests.exceptions as e:
        print("Exception occurred. Error :: ", e)
        raise SystemExit(e)

    try:
        zipcode_db = ZipCodeDatabase()
        zcd = zipcode_db[zip_code]
        city_name = zcd.city
        state = zcd.state
    except KeyError as ke:
        print("Not a valid zipcode. Please try again...")
        raise SystemExit(ke)
    return r, city_name, state

# Function to fetch weather forecast using city and state
def weather_city (api_key, city, state, unit):
    try:
        r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "," + state + "&appid=" + api_key + "&units=" + unit).json()
    except requests.exceptions.ConnectTimeout as ce:
        print("Connection timed out. Error message :: ", ce)
    except requests.exceptions.HTTPError as he:
        if he.code == 404:
            print("Connection timed out. Error message :: ", he)
    except requests.exceptions.RequestException as e:
        print(e)
        raise SystemExit(e)
    except requests.ConnectionError as cone:
        print(colored("Connection is not working", 'red'))
        raise SystemExit(cone)
    except requests.exceptions as e:
        print("Exception occurred. Error :: ", e)
        raise SystemExit(e)
    return r, city

# Main Function
def main():
    print("\n##################Welcome to Weather Forecast System##################")
    print("Time of execution : ", datetime.now())
    api_key = '4dd77355a2ad31d6b7a6f4a4c9154d18'
    state_list = {"AL": "Alabama", "AK": "Alaska", "AS": "American Samoa", "AZ": "Arizona", "AR": "Arkansas", "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "DC": "District Of Columbia", "FM": "Federated States Of Micronesia", "FL": "Florida", "GA": "Georgia", "GU": "Guam", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MH": "Marshall Islands", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York", "NC": "North Carolina", "ND": "North Dakota", "MP": "Northern Mariana Islands", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon", "PW": "Palau", "PA": "Pennsylvania", "PR": "Puerto Rico", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VI": "Virgin Islands", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming" }
    cont = "Y"

    # while loop to allow user to request weather forecast as many times user wants
    while cont == 'Y' or cont == 'y':
        internet_on()
        temp_unit = ''
        state = ''
        unit = ''
        unit_postfix = ''
        r = {}
        city = input("Please enter city or zip code : ")

        # If user enter a city name instead of zip then ask user to enter state abbreviation
        if not city.isdigit():
            while state == '':
                state_ab = input("Please enter State abbreviation : ")

                # for loop to fetch state name from state abbreviation
                for key, value in state_list.items():
                    if key == state_ab.upper():
                        state = value
                        break               # come out of for loop if state found
                    else:
                        state = ''
                if state == '':             # if state is not found then ask to enter again
                    print("Not a valid state abbreviation. Please enter it again...")

        # Asking user for unit of temperature they prefer
        while temp_unit.upper() != 'F' and temp_unit.upper() != 'C' and temp_unit.upper() != 'K':
            temp_unit = input("Enter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin : ")
            if temp_unit.upper() == 'F':
                unit = 'imperial'
                unit_postfix = '°F'
            elif temp_unit.upper() == 'C':
                unit = 'metric'
                unit_postfix = '°C'
            elif temp_unit.upper() == 'K':
                unit = 'kelvin'
                unit_postfix = 'K'
            else:
                print("Not a valid unit of temperature. Please enter either F or C...")

        # API Call to fetch weather based on zip code
        if city.isdigit():
            r, city_name, state = weather_zip(api_key, city, unit)
            for key, value in state_list.items():
                if key == state.upper():
                    state = value
                    break               # come out of for loop if state found

        # API Call to fetch weather based on city and state
        elif city.isalnum():
            r, city_name = weather_city(api_key, city, state, unit)

        for key, value in r.items():
            if key == 'cod' and value != 200:
                print(colored("########## Error Occurred ##########", 'red'))
                print(colored("Error Code :: " + value, 'red'))
            if key == 'message':
                print(colored("Error Message :: " + value, 'red'))
                print(colored("####################################", 'red'))
                exit(1)


        # Reading the JSON response and extracting value from it

        city_name = str(r['name'])
        temp = str(r['main']['temp']) + unit_postfix
        feels_like = str(r['main']['feels_like']) + unit_postfix
        temp_range = str(r['main']['temp_min']) + unit_postfix + ' - ' + str(r['main']['temp_max']) + unit_postfix
        desc = str(r['weather'][0]['description']).title()
        sunrise_int = int(r['sys']['sunrise'])
        sunset_int = int(r['sys']['sunset'])
        sunrise = datetime.fromtimestamp(sunrise_int).strftime("%I:%M:%S %p")
        sunset = datetime.fromtimestamp(sunset_int).strftime("%I:%M:%S %p")
        humidity = str(r['main']['humidity']) + '%'
        pressure = str(r['main']['pressure']) + ' hPa'

        # Printing weather Forecast
        print('\n')
        print('  ----------------------------------------------------')
        print(colored('                   Weather Forecast', 'blue'))
        print('  ----------------------------------------------------')
        print('                 City : ' + city_name + ', ' + state)
        print('        Date and Time : ', datetime.now().strftime("%m/%d/%Y %I:%M:%S %p"))
        print('  ----------------------------------------------------')
        print(colored('          Cloud Cover : ' + desc, 'green'))
        print(colored('          Temperature : ' + temp, 'green'))
        print(colored('          Feels Like  : ' + feels_like, 'green'))
        print(colored('          Temp Range  : ' + temp_range, 'green'))
        print(colored('          Humidity    : ' + humidity, 'green'))
        print(colored('          Pressure    : ' + pressure, 'green'))
        print(colored('          Sunrise     : ' + str(sunrise), 'green'))
        print(colored('          Sunset      : ' + sunset, 'green'))
        print('  ----------------------------------------------------')


        cont = input("Would you like to perform another weather lookup? (Y/N):")


if __name__ == '__main__':  # To check if current module is main
    main()
