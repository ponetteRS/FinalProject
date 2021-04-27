from bs4 import BeautifulSoup
import requests
import unittest
import json
import sqlite3
import os
import matplotlib.pyplot as plt

# Project artist: Music Madness
# artists: Ponette Rubio
# artists of Partners: Ponette Rubio and Jenny Siegel

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
    conn = sqlite3.connect(path+'/'+ "1finaldatabase.db")
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
#Saves album data to a database#

list_of_artists = billboard_list()   
#throughout the rest of the project, list_of_artists is the global variable for all 100 artists 
    
test = 0
# Get the artist on Billboard 100
def artist_weeks():
    cur.execute("CREATE TABLE IF NOT EXISTS artistWeeks (artist TEXT PRIMARY KEY, num_weeks INTEGER)")
    cur.execute("SELECT num_weeks FROM artistWeeks") #CHECK THE SELECT STATEMENT
    
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
             num_weeks = temp.split()[0] #number of weeks on the billboard
             cur.execute("INSERT OR IGNORE INTO artistWeeks (artist, num_weeks) VALUES (?, ?)", (artist, num_weeks))
            #  d[artist] = num_weeks #quick testing
    # return d
    conn.commit()

# returns list of top 10 artists
def top_ten():
    cur.execute('SELECT text FROM artistweeks ORDER BY weeks DESC') #none should self filter out
    all_artists = cur.fetchall()
    top = []
    for artist in all_artists[:10]:
        top.append(artist)
    return top

# creates 2 graphs from the Genius Lyrics info and iTunes database
def graphics():
    pass

# Tests for artist_weeks()
# print(artist_weeks())

# artist_weeks()
# print(top_ten()) 

def main():
    #creating fileartist
    path = os.path.dirname(os.path.realpath(__file__))
    cur, conn = setUpDatabase()
    # artist_weeks()
    # print(top_ten())


if __name__ == "__main__":
    main()
