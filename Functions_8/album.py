
def make_album(artist_name, album_name, num=None):
    album = {
        'artist': artist_name.title(),
        'album': album_name.title(),
    }
    if num:
        album['num_songs'] = num
        
    return album

print("enter 'q' for quit\n")

while True:
    artist_name = input("Enter the name of the artist: ")
    if artist_name == 'q':
        break
    album_name = input("Enter the album name: ")
    if album_name == 'q':
        break
    album = make_album(artist_name, album_name)
    print(album)

print("\nThanks for responding")