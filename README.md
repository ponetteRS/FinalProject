## FinalProject

## Initial Project Goals and Problems Faced
Our project goals have changed significantly since the project began. Initially, our goals were to gather data from the iTunes API, to gather information from the Genius Lyrics Website, to calculate the artist with the most songs and albums on iTunes, to calculate the most "popular" artist on Genius (based on the number of likes on their Genius page), and to then then to compare these data points to see if the most popular artists on Genius also had the largest iTunes discographies. 

Unfortunately, we faced many issues when trying to reach these goals: we were unable to scrape the likes off of the Genius Lyrics website using BeautifulSoup, and the calculations we had planned to do for the iTunes API were not useful for making any charts or graphs, so we had to change our project goals. 

## Final Project Goals
After lots of troubleshooting and research, our project goals were as follows:

From the iTunes API, Our Goals Were:

- To test whether iTunes filters all their searches the same way, specifically: in a search for just songs, does iTunes simply return the top songs from the most popular albums, or is a different method used?
  - To test this theory, we sought to find and calculate the overlap between iTunes searches for only songs and iTunes searches for only albums (using the iTunes API)
  - To do this, our goal was to create 2 database tables: One of the data returned in an iTunes search for only an artist's songs, and another of the data returned in an iTunes search for only an artist's albums
  - We then sought to make a scatterplot of the overlap between the searches, to see if any trends emerged

From the Billboard Website, Our Goals Were:

- To find the top 10 artists on the Billboard Artist 100 Charts, as well as how many weeks they had each been on the charts (using BeautifulSoup to scrape information from the Billboard website)
- To create a database table of this information
- To use this information to create a pie chart of the top 10 artists and the number of weeks they had remained on the charts
- To use this information to create a second pie chart, this time of the ......

## Instructions for Running the Code
Everything should be set up when the files are downloaded. To run the code, simply:
1. Hit the play button- this will upload the first 25 rows to the database and produce our 3 vizualizations
2. Hit the play button 3 more times- each time this is done, 25 new rows of unique data will be uploaded to each table. After running the code a total of 4 times, there should be 100 rows in each table.
3. After the code has been ran 4 times, our csv file (INSERT NAME HERE) will be fully populated, and will match the csv we turned in in our Zip file project submission.

## Code Documentation

billboard_list()
- takes in no inputs
- scrapes the artists' names off the Billboard Artist 100 Website using BeautifulSoup 
- returns a list of all the artist's names on the Billboard Artist 100 Website


setUpDatabase()
- takes the name of a database as input
- creates the database
- returns the database cursor (cur) and the database connection object (conn)



iTunes_songs()
- takes in a list of the names of the top 10 artists on the Billboard Artist 100 as input
- creates a JSON object of the Songs in an iTunes Search for each artist's SONGS ONLY (up to 25 songs per artist)
- returns a list whose items are each a JSON formatted data structure of the iTunes search for the songs of every artist on the Billboard 100


iTunes_albums()
- takes a list of the names of the top 10 artists on the Billboard Artist 100 as input
- creates a JSON object of the Albums in an iTunes Search for each artist's ALBUMS ONLY (up to 25 albums per artist)
- returns a list whose items are each a JSON formatted data structure of the iTunes search for the albums of every artist on the Billboard 100


songs_table()
- takes in the database cursor object, the database connection object, and the list of artists names on the Billboard Artist 100 as inputs
- saves data from songs-only iTunes searches to a table called Songs
- the table has 4 columns- the song title, the album title, the artist's name, and the song's numeric id within iTunes
- returns nothing


albums_table()
- takes in the database cursor object, the database connection object, and the list of artists names on the Billboard Artist 100 as inputs
- saves data from albums-only iTunes searches to a table called Albums
- the table has 3 columns- the album title, the artist's name, and the album's numeric id within iTunes
- returns nothing


artist_weeks()
- takes in the database cursor object and the database connection object as inputs
- Scrapes the artists' names and the number of weeks they have been on the Billboard Artist 100 from the Billboard Website, and saves it to a table called 
  artistWeeks
- returns nothing

top_ten()
- uses BeautifulSoup to scrape the Billboard Hot 100 website
- scrapes the artists' names and the number of weeks they have been on the Billboard Artist 100 from the Billboard Website, and saves it to a dictionary
- returns a dictionary used for the pie chart visualizatio

most_music()
- takes in the database cursor object and the database connection object as inputs
- calculates the number of songs from the Songs table that are on albums in the Albums table (if there are no songs in the songs table on an album in the albums  
  table, that album is ignored: these calculations are solely meant to measure when there is overlap between the 2 tables.) (ie. calculates the overlap between a search for an artist's songs on iTunes and searches for that artist's albums on iTunes).
- also calculates the average number of weeks an artist has been on the Billboard Artist 100 charts, as well as the actual number of weeks each artist has been on the Artist 100 charts
- writes all of the calculations to the Music_Calculations.csv file
- returns a dictionary of each album in the Albums table with songs in the Songs table as keys and the number of songs that album has in the Songs table as values

scatterplot()
- takes in what is returned from most_music() (a dictionary of each album in the albums table, and the number of songs it has in the songs table (if that is more than 0)) as input
- creates a scatterplot of the number of songs in the Songs table that are on albums in the Albums table

pie()
- has no inputs
- creates a pie chart of the number of weeks the top ten artists currently on the Billboard Artist 100 Charts have remained on the Billboard Artist 100 Charts 

main()
- takes in no inputs
- calls every function we created, with the specified inputs stated above
- returns nothing

Resources Used:

Date: | Issue Description | Location of Resource | Result | 
----- | ----------------- | -------------------- | -------|
4/22 | struggling to figure out how to make labels fit size constraints for a matplotlib scatterplot |https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib | labeling issue resolved; margins still to be figured out | 
4/22 | struggling to figure out what graph to use for calculations done from data collected from iTunes API | Office Hours w/ Ashley | Issue resolved- decided to re-do calculations to creata data that would suit a scatterplot |
4/26 | Could not scrape info from Genius Webpage; Struggling to figure out Limit 25 table constraint | Office Hours w/ AJ | Issue resolved- Opted to use Billboard Website instead of Genius | 
