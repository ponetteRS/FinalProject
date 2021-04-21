from bs4 import BeautifulSoup
import re
import requests
import unittest
<<<<<<< HEAD
import json
=======
<<<<<<< HEAD
# import sqlite3
# import json
# import os

#
# Project Name: Music Madness
# Names: Ponette Rubio
#
=======
>>>>>>> 05a3fd14d22a2442de0639529dda63d3a37e27a3

#Names of Partners: Ponette Rubio and Jenny Siegel

#Creates a list of 100 artists using the Billboard Artist 100 Website
def billboard_list():
    url = 'https://www.billboard.com/charts/artist-100'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    lst = []
    data = soup.find('div', class_ = 'chart-details')
    rows = data.find_all('div', class_  = "chart-list-item")
    

<<<<<<< HEAD
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
=======
list_of_artists = billboard_list()   
#throughout the rest of the project, list_of_artists is the global variable for all 100 artists 
>>>>>>> 7a70d5f6f4d1c190544c8c7163179eb2de25bdcc


# converts artist name to the url ending in the Genius url format
# ex Ariana-grande, Lady-gaga, Rihanna, etc.
def reformat(artist):
    reformatted_artist = artist
    #Makes first char upper case and rest of string lower case if two words
    reformatted_artist = reformatted_artist[0].upper() + reformatted_artist[1:].lower()
    #adds the - that url has
    reformatted_artist = reformatted_artist.replace(' ', '-')
    

# Get the artist with most likes from Genius website from artists from billboard
# This will be done by collecting the number of likes that artist got on their page/artist description
def artist_likes():
    artists_list = billboard_list() #list of artists from which to gather like data
    url = 'https://genius.com/artists/'
    likes_d = {}
    
    for artist in artists_list:
        url += reformat(artist) #adds artist name to the url ending in the Genius url format
        # ex. on genius, Ariana-grande, Lady-gaga, Rihanna, etc.
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

    return likes_d

# from the dict of artists will get the most liked artist
def most_likes():
    
    return sorted(artist_likes(), reverse = True)
>>>>>>> 05a3fd14d22a2442de0639529dda63d3a37e27a3

# will import like information into the database
def import_likes():
    pass

# creates 2 graphs from the Genius Lyrics info and iTunes database
def graphics():
    pass

#throughout the rest of the project, list_of_artists is the global variable for all 100 artists
#def main(): 
#    list_of_artists = billboard_list() 
#    for artist in list_of_artists:
#        songs = iTunes_songs(artist)
#        albums = iTunes_albums(artist)

<<<<<<< HEAD
# tests
=======
>>>>>>> 7a70d5f6f4d1c190544c8c7163179eb2de25bdcc

