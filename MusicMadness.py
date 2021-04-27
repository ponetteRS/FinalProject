from bs4 import BeautifulSoup
import requests
import unittest
import json
import sqlite3
import os
import re
import numpy as np
import matplotlib.pyplot as plt

# Project artist: Music Madness
# names: Ponette Rubio
# names of Partners: Ponette Rubio and Jenny Siegel
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
# Create Database
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

#Creates JSON object of the first 25 Songs in an iTunes Search for each artist within lst
def iTunes_songs(lst):
    url= 'https://itunes.apple.com/search'
    final = []
    for l in lst:
        param= {'term': l, 'media' : 'music', 'entity': 'song', 'limit': '25'}  
        songs= requests.get(url, params= param)
        song_data = songs.json()
        final.append(song_data)
    return final

#Creates JSON object of the first 25 albums in an iTunes Search for each artist within lst
def iTunes_albums(lst):
    url= 'https://itunes.apple.com/search'
    final = []
    for l in lst:
        param= {'term': l, 'entity': 'album', 'limit': '25'}  
        albums= requests.get(url, params= param)
        album_data = albums.json()
        final.append(album_data)
    return final

#Saves data from songs-only iTunes searches to a table called Songs
#The table has 4 columns- the song title, the album title, the artist's name, and the song's numeric id within iTunes
def songs_table(cur, conn, lst):
    cur.execute("CREATE TABLE IF NOT EXISTS Songs (song_title TEXT, album TEXT, artist TEXT, id INTEGER PRIMARY KEY)")
    count = 0
    for item in lst:
        for dct in item['results']:
            if count == 25:
                break
            else:  
                song = dct['trackName']
                album = dct['collectionName']
                artist = dct['artistName']
                iTid = dct['trackId']
                if cur.execute("SELECT song_title AND artist AND album FROM Songs WHERE song_title = ? AND artist = ? AND album = ?", (song, artist, album,)).fetchone() == None:
                    cur.execute("INSERT INTO Songs (song_title, album, artist, id) VALUES (?,?,?,?)", (song, album, artist, iTid))
                    count += 1
    conn.commit()

#Saves data from albums-only iTunes searches to a table called Albums
#The table has 3 columns- the album title, the artist's name, and the album's numeric id within iTunes
def albums_table(cur, conn, lst):
    cur.execute("CREATE TABLE IF NOT EXISTS Albums (album_title TEXT, artist TEXT, id INTEGER PRIMARY KEY)")
    count = 0
    for item in lst:
        for dct in item['results']:
            if count == 25:
                break
            else:
                artist = dct['artistName']
                album = dct['collectionName']
                iTid = dct['collectionId']
                if cur.execute("SELECT album_title AND artist FROM Albums WHERE album_title = ? AND artist = ?", (album, artist,)).fetchone() == None:
                    cur.execute("INSERT INTO Albums (album_title, artist, id) VALUES (?,?,?)", (album, artist, iTid))
                    count += 1
    conn.commit()
    
#if cur.execute("SELECT album_title AND artist FROM Albums WHERE album_title = ? AND artist = ?", (album, artist)) == None:



#Creates JSON object of up to 10 albums per artist
def iTunes_albums(artist):
    url= 'https://itunes.apple.com/search'
    param= {'term': artist, 'entity': 'album', 'limit': '10'}  
    iTunes= requests.get(url, params= param)
    data= json.loads(iTunes.text)
    return data
#Saves album data to a database#

# Get the artist on Billboard 100
def artist_weeks(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS artistWeeks (artist TEXT PRIMARY KEY, num_weeks INTEGER)")
    count = 0
    
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
             if count == 25:
                break
             else:
                artist= ar.text.strip()
                temp = stats_row[2].text
                num_weeks = temp.split()[0] #number of weeks on the billboard
                if cur.execute("SELECT artist AND num_weeks FROM artistWeeks WHERE artist = ? AND num_weeks = ?", (artist, num_weeks,)).fetchone() == None:
                    cur.execute("INSERT INTO artistWeeks (artist, num_weeks) VALUES (?,?)", (artist, num_weeks))
                    count += 1
            #  d[artist] = num_weeks #quick testing
    # return d
    conn.commit()

# returns dictionary of top 10 artists as keys and weeks as values to be used in pie
def top_ten():
    cur.execute('SELECT artist AND num_weeks FROM artistweeks ORDER BY num_weeks DESC') 
    all_artists = cur.fetchall()
    top = {}
    i = 0 
    for artist in all_artists[:10]:
        top = top.get(artist, 0) + artist[i]
        i += 1
    return top

#Create a scatterplot of the number of songs in the Songs table that are on albums in the Albums table
def scatterplot(data):
    albums = []
    num_songs = []

    for d in data.items():
        albums.append(d[0].strip())
        num_songs.append(d[1])
    
    plt.figure(figsize = (10,8))
    plt.scatter(x = albums, y = num_songs)
    plt.title('Songs and Album Overlap Between iTunes Searches for Songs and Albums')
    plt.xlabel('Album Names')
    plt.ylabel('Number of Songs per Album')
    plt.xticks(rotation = 90)
    plt.show()

# 
def pie():
    d = top_ten()
    artists = []
    values = []
    i = 0 
    for key in d: #creates two data lists needed for visualization
        artists.append(key)
        values.append(key[i])
        i += 1
    # Creating explode data
    explode = (0.2, 0.0, 0.0, 0.0, 0.0, 0.0)

    # Creating color parameters
    colors = ( "orange", "cyan", "brown", "grey", "indigo", "beige", "cyan", "brown", "grey", "indigo")

    # Wedge properties
    wp = { 'linewidth' : 1, 'edgecolor' : "grey" }

    # Creating autocpt arguments
    def func(pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)
    
    # Creating plot
    fig, ax = plt.subplots(figsize =(10, 7))
    wedges, texts, autotexts = ax.pie(values, 
                                    autopct = lambda pct: func(pct, values),
                                    explode = explode, 
                                    labels = artists,
                                    shadow = True,
                                    colors = colors,
                                    startangle = 90,
                                    wedgeprops = wp,
                                    textprops = dict(color ="magenta"))
    # Adding legend
    ax.legend(wedges, artists,
            title ="Artists",
            loc ="center left",
            bbox_to_anchor =(1, 0, 0.5, 1))
    
    plt.setp(autotexts, size = 8, weight ="bold")
    ax.set_title("Pie chart of artists and number of weeks on charts")
    # show plot
    plt.show()
    
#Of the 10 most popular artists calculate the number of songs from the Songs table that are on 
#albums in the Albums table. If there are no songs in the songs table on an album in the albums table, that album is ignored.
#These calculations are solely meant to measure when there is overlap between the 2 tables.  
def most_music(cur, conn):

    cur.execute("SELECT Songs.artist, Songs.song_title, Albums.album_title FROM Songs JOIN Albums WHERE Songs.album = Albums.album_title")
    music = cur.fetchall()

    music_data = {}
    for i in range(len(music)):
        if music[i-1][2] == music[i][2]:
            music_data[music[i][2]] = music_data.get(music[i][2], 0) + 1
        else:
            continue

    with open('iTunes.csv','w') as f:
        f.write('Of the albums in the Albums table: \n\n')
        for album in music_data.items():
            f.write(album[0] + " has " + str(album[1]) + ' song(s) in the Songs table \n')
            
    f.close()
    return music_data  
# Tests for artist_weeks()
# print(artist_weeks())

# artist_weeks()
# print(top_ten()) 

def main():
    #creating filename
    path = os.path.dirname(os.path.realpath(__file__))
    cur, conn = setUpDatabase('iTunes.db') #change this to be named Music on final file
    songs = iTunes_songs(list_of_artists[:10])
    # albums = iTunes_albums(list_of_artists[:10]) 
    # songs_table(cur, conn, songs)
    # albums_table(cur, conn, albums)
    # music_data = most_music(cur, conn)
    # scatterplot(music_data)
    artist_weeks(cur, conn)
    # print(top_ten())


if __name__ == "__main__":
    main()
