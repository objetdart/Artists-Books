import csv

MoMA_Americans = {}

with open("Artworks.csv", "r") as MoMA_Americans:

    artist_nationality = csv.reader(MoMA_Americans)

    for moma_row in artist_nationality:
        artistName = moma_row[1]
        artistBio = moma_row[2]

        if 'American, born' in artistBio:
            print(artistName)
            print(artistBio)
