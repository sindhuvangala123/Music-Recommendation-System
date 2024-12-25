data = {
    'Song-Name': ['Aankh Marey', 'Lungi Dance', 'Shape of You', 'Senorita', 'Blinding Lights'],
    'Singer/Artists': ['Mika Singh', 'Honey Singh', 'Ed Sheeran', 'Shawn Mendes', 'The Weeknd'],
    'Genre': ['Bollywood', 'Bollywood', 'Pop', 'Latin Pop', 'Synthwave'],
    'Album/Movie': ['Simmba', 'Chennai Express', 'Divide', 'Shawn Mendes', 'After Hours']
}
# Display the song list

for index, song in enumerate(data['Song-Name'], start=1):
    print(f"{index}. {song}")

# Ask user to select a song
selected_song = input("Please select a song to recommend: ")

# Check if the selected song exists in the list
if selected_song in data['Song-Name']:
    # Find the index of the selected song
    song_index = data['Song-Name'].index(selected_song)

    # Display the information related to the selected song
    print(f"\nInformation about '{selected_song}':")
    print(f"Singer/Artist: {data['Singer/Artists'][song_index]}")
    print(f"Genre: {data['Genre'][song_index]}")
    print(f"Album/Movie: {data['Album/Movie'][song_index]}")
else:
    print("Song not found, please choose a valid song from the list.")
