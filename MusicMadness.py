from bs4 import BeautifulSoup
import re
import requests
import unittest
<<<<<<< HEAD
# import sqlite3
# import json
# import os

#
# Project Name: Music Madness
# Names: Ponette Rubio
#
=======

#Names of Partners: Ponette Rubio and Jenny Siegel

#Create a list of 100 artists using the Billboard Artist 100 Website
def billboard_list():
    url = 'https://www.billboard.com/charts/artist-100'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    lst = []
    data = soup.find('div', class_ = 'chart-details')
    rows = data.find_all('div', class_  = "chart-list-item")
    
    for row in rows:
        art = row.find_all('span', class_ = "chart-list-item__title-text")
        for a in art:
            artist= a.text.strip()
            lst.append(artist)
    return lst

list_of_artists = billboard_list()   
#throughout the rest of the project, list_of_artists is the global variable for all 100 artists 
>>>>>>> 7a70d5f6f4d1c190544c8c7163179eb2de25bdcc




<<<<<<< HEAD
# tests
=======
>>>>>>> 7a70d5f6f4d1c190544c8c7163179eb2de25bdcc

