"""
    Name: apod_class.py
    Author: 
    Created:
    Purpose: Get NASA APOD API
    NASA Astronomy photo of the day
"""

# Import the requests module
import requests
from datetime import date
from api_key import api_key
IS_DEBUGGING = False


class APODClass:
    def __init__(self):
        pass

    def get_data(self):

        URL = "https://api.nasa.gov/planetary/apod"

        # Get date from calendar widget
        # date = self.calender.get_date()
        display_date = date.today()
        # Set up parameters for request
        parameters = {
            'api_key': api_key,
            'date': display_date
        }
        # Use the requests.get() function
        # with the parameter of the URL, params, and timeout
        response = requests.get(
            URL,
            params=parameters,
            timeout=3
        )

        # If the status_code is 200, successful connection and data
        if (response.status_code == 200):

            # Convert the JSON data into a Python dictionary with key value pairs
            data = response.json()

            # Used to debug process
            if (IS_DEBUGGING == True):

                # Display the status code
                print(
                    f'\nThe status code for this API request is {response.status_code} \n')

                # Display the raw JSON data from the API
                print('The raw data from the API:')
                print(response.text)

                # Display the Python dictionary
                print('\nThe JSON data converted to a Python dictionary:')

            return (data.get("explanation"))

        else:
            print(f"API unavailable: {response.status_code}")
