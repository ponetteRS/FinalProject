from bs4 import BeautifulSoup
import requests
import unittest
import json
import sqlite3
import os
import matplotlib.pyplot as plt

# Project Name: Music Madness
# Names: Ponette Rubio
# Names of Partners: Ponette Rubio and Jenny Siegel

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

def setUpDatabase():
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+ "finaldatabase.db")
    cur = conn.cursor()
    return cur, conn

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
    
    return reformatted_artist
    

# Get the artist with most likes from Genius website from artists from billboard
# This will be done by collecting the number of likes that artist got on their page/artist description
def artist_likes():
    # setUpDatabase() #temp until main merge
    # cur.execute("CREATE TABLE IF NOT EXISTS artistsLikes (name TEXT PRIMARY KEY, likes INTEGER)")
    # cur.execute("SELECT likes FROM artistsLikes")
    
    url = 'https://www.billboard.com/charts/artist-100'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    d = {}
    data = soup.find('div', class_ = 'chart-details')
    rows = data.find_all('div', class_  = "chart-list-item")

    for row in rows:
         artist_row = row.find_all('span', class_ = "chart-list-item__title-text")
         stats_row = row.find_all('div', class_ = "chart-list-item__ministats-cell")

         for ar in artist_row:
             artist= ar.text.strip()
             temp = stats_row[2].text
             weeks = temp.split()[0] #number of weeks on the billboard
             d[artist] = weeks #quick testing
    return d
   
    # for artist in artists_list:
    #     try: 
    #         artist = str(reformat(artist))
    #         temp_url = url + artist #adds artist name to the url ending in the Genius url format
    #         # print(temp_url) #urls go to right website
    #         r = requests.get(url)
    #         soup = BeautifulSoup(r.text, 'html.parser')
    #         data = soup.find('div', class_= 'voting-total square_button square_button--transparent voting-total--positive')
    #         # print(data)
        
    #         likes_d[artist] = data #dict to see changes
    #         # will import like information into the database
    #         # cur.execute("INSERT OR IGNORE INTO artistsLikes (name, likes) VALUES (?, ?)", (name, likes))
    #     except:
    #         likes_d[artist] = 0 #artists not on Genius get no likes
    # # conn.commit()
    # return likes_d

# returns list of top 10 artists
def top_ten():
    cur.execute('SELECT text FROM artistLikes ORDER BY likes DESC') #none should self filter out
    all_artists = cur.fetchall()
    top = []
    for artist in all_artists[:10]:
        top.append(artist)
    return top

# creates 2 graphs from the Genius Lyrics info and iTunes database
def graphics():
    pass


# tests for reformat(artist)
# reformatted_artist = 'Ariana Grande'
# # reformatted_artist = 'Rihanna'
# reformatted_artist = reformatted_artist[0].upper() + reformatted_artist[1:].lower()
# reformatted_artist = reformatted_artist.replace(' ', '-')
# print(reformatted_artist)

# Tests for rartist_likes()
print(artist_likes())
                            ######## calls to be added to main ########

# setUpDatabase() #run when fixed scrape issue
# artist_likes()
# print(top_ten()) 


