from bs4 import BeautifulSoup
import re
import requests
import unittest
# import sqlite3
# import json
# import os

#
# Project Name: Music Madness
# Names: Ponette Rubio
#

#Names of Partners: Ponette Rubio and Jenny Siegel

#Create a list of 100 artists using the Billboard Artist 100 Website
def billboard_list():
    url = 'https://www.billboard.com/charts/artist-100'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    lst = []
    data = soup.find('div', class_ = 'chart-details')
    rows = data.find_all('div', class_  = "chart-list-item")
    

list_of_artists = billboard_list()   
#throughout the rest of the project, list_of_artists is the global variable for all 100 artists 


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
        try:
            url += reformat(artist) #adds artist name to the url ending in the Genius url format
            # ex. on genius, Ariana-grande, Lady-gaga, Rihanna, etc.
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
        except:
            print('')

    return likes_d

# from the dict of artists will get the most liked artist
def most_likes():
    
    return sorted(artist_likes(), reverse = True)

# will import like information into the database
def import_likes():
    pass

# creates 2 graphs from the Genius Lyrics info and iTunes database
def graphics():
    pass


# tests

