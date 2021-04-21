from bs4 import BeautifulSoup
import re
import requests
import unittest
import json

#Names of Partners: Ponette Rubio and Jenny Siegel

#Creates a list of 100 artists using the Billboard Artist 100 Website
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

#Creates JSON object of up to 25 songs per artist
def iTunes_songs(artist):
    url= 'https://itunes.apple.com/search'
    param= {'term': artist, 'entity': 'song', 'limit': '25'}  
    iTunes= requests.get(url, params= param)
    data= json.loads(iTunes.text)
    return data
    
#Saves song data to a database
#def songs_table(cur, conn):

#Creates JSON object of up to 10 albums per artist
def iTunes_albums(artist):
    url= 'https://itunes.apple.com/search'
    param= {'term': artist, 'entity': 'album', 'limit': '10'}  
    iTunes= requests.get(url, params= param)
    data= json.loads(iTunes.text)
    return data
    
#Saves album data to a database



#throughout the rest of the project, list_of_artists is the global variable for all 100 artists
#def main(): 
#    list_of_artists = billboard_list() 
#    for artist in list_of_artists:
#        songs = iTunes_songs(artist)
#        albums = iTunes_albums(artist)


