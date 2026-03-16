# AFL University Player Game Counts
Scrapes game and player data for University teams from PlayHQ and loads a cleaned dataframe containing player information into a relational database.

# Features
- Fetches fixtures for all University teams in a given PFL season
- Scrapes player participants per game via PlayHQ's GraphQL API
- Aggregates total appearances per player across all grades and seasons for University
- Writes a sorted 'players' table to a database using SQLAlchemy

# Tech Stack
- Python3
- Jupyter Notebook
- Requests, Multithreading, Pandas, SQLAlchemy
