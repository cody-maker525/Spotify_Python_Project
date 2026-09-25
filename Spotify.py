# python numbers
import pandas as pd


import matplotlib.pyplot as plt
import numpy as np
import csv
import json

# data analysis library


# with open("Liked_Songs.csv",mode="r" ,encoding="utf-8", newline="") as f:
#     data = csv.reader(f)
#     for row in data:
#         print(row)

df = pd.read_csv('Liked_Songs.csv')
#print(df)

#df['genres] selects genres col from table
#.dropna removes row where genres is missing
#.str.split with explode = if more than one value split, then treat separately
#str.strip removes trailing whitespace
genres = df['Genres'].dropna(). str.split(',').explode().str.strip()

#value counts= how many times each unique value appears
genre_counts = genres.value_counts()

top15 = genre_counts.head(15)

top15.plot(kind="bar")
plt.title('Top 15 Genres')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#tight layout adjusts spacing





# map to plot points
# import matplotlib.pyplot as plt

# python visualization library, based on matplotlib
# import seaborn as sns 

#SET UP JSON FILE TO CSV
# json_data = 

# # use pandas data to read dataset from csv
# sp_data = pd.read_csv(
#     "my_streaming_history.csv", on_bad_lines="skip"
# )  # put spotify data tracks here
# sp_tracks = pd.read_csv(
#     "spotify_features_merged.csv", on_bad_lines="skip"
# )  # put spotify features

# n = 10

# # viewing my data
# print(sp_tracks.columns.tolist())
# print(sp_data.columns.tolist())

# # print(sp_data.head(n))  # not added yet
# print("TOP 10")
# print(sp_tracks[["Track Name", "Artist Name(s)", "Genres"]].head(n))  # tracks data

# print(pd.isnull(sp_data).sum())  # return number of missing values in data

# print(pd.isnull(sp_tracks).sum())  # return number of missing values in data
# # print("TRACK INFO")
# # print(sp_data.info())  # prints info from data frame

# # print(sp_tracks.info())
# # print("LEAST POPULAR SONGS I HOPE")
# # # 10 least popular songs in spotify dataset
# # a = sp_tracks.sort_values("Popularity", ascending=True)[
# #     0:10
# # ]  # 0:10 = first 10 rows, rows 0-10 by index
# # print(a[["Track Name", "Popularity", "Artist Name(s)"]])  # [[]] = multiple columns

# # # describes and flips so rows become columns
# # # sp_data.describe().transpose()
# # print("TRANSPOSE THING")
# # sp_tracks.describe().transpose()
# # print("COLUMNS FOR STREAMING")
# # print(sp_data.head(10))
# # print(sp_data.columns.toList())
# # print("MOST PLAYED")
# # play_counts = sp_data["master_metadata_track_name"].value_counts()
# # print(play_counts.head(10))
# # # a = sp_tracks
# # # b = a[["popularity" > 90].sort_values("popularity", ascending=False)[:10]]
# # # # 0:10 = first 10 rows, rows 0-10 by index
# # # b[["name", "popularity", "artists"]]

# # print("INDEX NIGHTMARE")
# # # make release date column as index column
# # print(sp_tracks.index[:5])
# # print(type(sp_tracks.index[0]))
# # rDate = sp_tracks
# # rDate = sp_tracks.set_index("Release Date")
# # rDate.index = pd.to_datetime(rDate.index, errors="coerce")
# # rDate = rDate.sort_index(ascending=True)[0:10]
# # print(rDate[["Name", "Artist Name(s)", "Genres"]].head(10))
# # print(rDate.head(10))
# # print(rDate.index.isna().sum())
# # #TODO fix headers