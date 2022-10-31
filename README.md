# NASA APOD App in Python Pyside6
## Project Description
NASA Astronomy Photo of the Day

Example project for Intro to Computer Science 1 Think Aloud Individual Project.

## Requirements
 Python 3.10.8
 PySide 6.4.0.1
 - pip install pyside6
 - pip install requests

## Changes
- 10-30-22: Resize HD photo to fit vertical size of screen
- 10-23-22: Add random photo button
- 10-15-22: Add QTimer to allow GUI to show before getting initial APOD
- 10-15-22: Add tooltips
- 10-15-22: Click thumbnail to display full photo
- 10-15-22: Display hd photo
- 10-08-22: Display full photo
- 10-07-22: Show thumbnail of current day's APOD
- 10-08-22: Display image or YouTube video
- 09-29-22: Calendar widget chooses that days APOD
- 09-29-22: Get and display current day's APOD description
- 09-20-22: Convert QT Designer file main_window.ui to main_ui.py
- 09-20-22: Design UI in QTDesigner 

## Version History
- (10-23-22) V4 Add retrieve random photo.
- (10-08-22) V3 Retrieve and display full and hd photo.
- (10-07-22) V2 Retrieve and display thumbnail.
- (09-27-22) V1 Connect to NASA APOD API. Retrieve and display current APOD description.

## UI Design
V3 GUI

![](/images/gui_design_3.png)

V1 GUI

![](/images/gui_design_1.png)

### License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Copyright (c) 2022 William A Loring
