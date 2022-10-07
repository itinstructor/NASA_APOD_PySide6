"""
    Name: apod_class.py
    Author: 
    Created:
    Purpose: Get NASA APOD API
    NASA Astronomy photo of the day
"""

# Import the requests module
from PySide6 import QtGui
import requests
from datetime import date
from api_key import api_key
IS_DEBUGGING = False


class APODClass:
    def __init__(self):
        """Class to get NASA APOD data from API"""
        self.img = QtGui.QPixmap()
        self.hd_img = QtGui.QPixmap()
        pass

    def get_img(self):
        return self.img
    
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
            return (self.response.get("explanation"))

        else:
            print(f"API unavailable: {response.status_code}")
    
    def get_photo(self):
        """Get the url from the request.
        
        Most of the time it is an image, sometimes is is a link to a
        YouTube video.
        """
        url = self.response["url"]
        if self.response["media_type"] == "image":
            # Get the hdurl response
            hdurl = self.response["hdurl"]
            # Stream=True sets automatic download
            img_response = requests.get(url, stream=True)
            hd_img_response = requests.get(hdurl, stream=True)

            # Get the content of the response and use BytesIO to open it as an image.
            # Keep a reference to this as this is what you can use to save (Image not PhotoImage)
            # Create the full screen image for the second window
            self.img.loadFromData(img_response.content)
            self.hd_img.loadFromData(hd_img_response.content)

            # Convert from bytes to image format
            # self.img = QtGui.QPixmap(img_data)
            # self.hd_img = QtGui.QPixmap(hd_img_data)
            # self.img = Image.open(BytesIO(img_data))
            # self.hd_img = Image.open(BytesIO(hd_img_data))

            # # Convert image into a format that Tkinter understands
            # self.full_img = ImageTk.PhotoImage(self.img)
            # self.hd_img = ImageTk.PhotoImage(self.hd_img)

            # Create a thumbnail for the main window
            # thumb = Image.open(BytesIO(img_data))
            # thumb.thumbnail((200, 200))
            # self.thumb = ImageTk.PhotoImage(thumb)

            # Set the thumnail image
            # self.lbl_thumbnail.config(image=self.thumb)
        # else:
        #     # We have a link to a video...open the video (try july 1st, 2020)
        #     self.lbl_thumbnail.config(image="")
        #     self.lbl_thumbnail.config(text=url)
        #     webbrowser.open(url)
