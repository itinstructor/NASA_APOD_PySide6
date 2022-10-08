"""
    Name: apod_class.py
    Author: 
    Created:
    Purpose: Get NASA APOD API
    NASA Astronomy photo of the day
"""

# Import the requests module
import webbrowser
from PySide6 import QtGui
# pip install requests
import requests
from datetime import date
from api_key import api_key
IS_DEBUGGING = False


class APODClass:
    def __init__(self):
        """Class to get NASA APOD data from API"""
        self._img = QtGui.QPixmap()
        self._hd_img = QtGui.QPixmap()
        self._explanation = ""

    @property
    def img(self):
        """Normal quality image."""
        return self._img

    @property
    def hd_img(self):
        """HD image."""
        return self._hd_img

    @property
    def explanation(self):
        """APOD photo explanation"""
        return self._explanation

#------------------------ GET DATA --------------------------------------------#
    def get_data(self, display_date):
        """Get APOD data from API."""
        # NASA APOD API URL
        APOD_URL = "https://api.nasa.gov/planetary/apod"

        # Set up parameters for request
        parameters = {
            'api_key': api_key,
            'date': display_date
        }
        # Use the requests.get() function
        # with the parameter of the URL, params, and timeout
        response = requests.get(
            APOD_URL,
            params=parameters,
            timeout=3
        )

        # If the status_code is 200, successful connection and data
        if (response.status_code == 200):

            # Convert the JSON data into a Python dictionary with key value pairs
            self.response = response.json()

            # Used to debug process
            if (IS_DEBUGGING == True):

                # Display the status code
                print(
                    f'\nAPI request status code: {response.status_code} \n')

                # Display the raw JSON data from the API
                print("API raw data:")
                print(response.text)

                # Display the Python dictionary
                print('\nJSON data converted to a Python dictionary:')
            self.get_photo()
            self._explanation = self.response.get("explanation")

        else:
            print(f"API unavailable: {response.status_code}")

#------------------------ GET PHOTO -------------------------------------------#
    def get_photo(self):
        """Get the url from the request.

        Most of the time it is an image, sometimes is is a link to a
        YouTube video.
        """
        # Get this property
        url = self.response["url"]
        self._img = QtGui.QPixmap()
        # Is the response an image or a link to a video
        if self.response["media_type"] == "image":
            # Get the hdurl response
            hdurl = self.response["hdurl"]
            # Stream=True sets automatic download
            img_response = requests.get(url, stream=True)
            hd_img_response = requests.get(hdurl, stream=True)

            # Load the image data from the response
            self._img.loadFromData(img_response.content)
            self._hd_img.loadFromData(hd_img_response.content)

        else:
            # We have a link to a video...open the video (try july 1st, 2020)
            self._img = None
            # self.lbl_thumbnail.config(text=url)
            webbrowser.open(url)
