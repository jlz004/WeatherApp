import json, requests
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def data(location):
    if location.lower() == 'q':
        quit()
    # Make the API call and store the information.
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    url = f"{base_url}?q={location}&units=imperial&APPID={os.getenv('appid')}"
    print("\n", url)

    # Check if the API response was successful.
    r = response = requests.get(url)
    print(f"Status Code: {r.status_code}")

    # Store the API response.
    try:
        unformated_data = response.json()

        # Print the API response information about temperature.
        temp = unformated_data["main"]["temp"]
        print(f"The current temp is: {temp}")

        temp_max = unformated_data["main"]["temp_max"]
        print(f"The max temp is: {temp_max}")

    # If input is invalid tell user to input valid data.
    except KeyError:
        print("Please enter a valid City or Zip Code")
        main()


def main():
    configure()
    while True:
        # Get the location.
        location = input("\nEnter a City, Zip Code, or q to Quit : ")
        data(location)


main()
