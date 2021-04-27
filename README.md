## FinalProject

## Initial Project Goals and Issues Faced
Our project goals have changed significantly since the project began. Initially, our goals were to gather data from the iTunes API, to gather information from the Genius Lyrics Website, to calculate the artist with the most songs and albums on iTunes, to calculate the most "popular" artist on Genius (based on the number of likes on their Genius page), and to then then to compare these data points to see if the most popular artists on Genius also had the largest iTunes discographies. Unfortunately, we faced many issues when trying to reach these goals: we were unable to scrape the likes off of the Genius Lyrics website using BeautifulSoup, and the calculations we had planned to do for the iTunes API were not useful for making any charts or graphs, so we had to change our project goals. 

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


## Specfic tasks completed
- [ ] Accessed at least 2 APIs or 1 API and 1 Website
- [ ] Store at least 100 items (rows) in at least one table per API/website
- [ ] Have at least 1 table per API/website. At least 1 API/website must have 2 tables that share a key.
- [ ] Limited the amount of data to 25 collected/stored at a time up to the first 100
- [ ] Selected items from all the tables and calculated something from the data (average, counts, etc)
- [ ] Database join used at least once in selecting the items
- [ ] Write a well-formatted, self explanatory file from the calculations (JSON, csv or text file)
- [ ] Visualization (2 for 2 persons in a team, 3 for 3 persons in a team)

