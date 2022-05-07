class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (artist): An artist object representing the songs creator
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        """
        Song init method

        :param title: str: Initializes the title
        :param artist: obj: Artist object representing the song
        :param duration: int: Initial value for the duration
        """
        self.title = title
        self.artist = artist
        self.duration = duration


# help(Song)
# help(Song.__init__)
# print(Song.__doc__)
# print(Song.__init__.__doc__)

class Album:
    """Class to represent an album using a tracklist
    Attributes:
        album_name (str): The name of the album
        year (int): The year the album was released
        artist (Artist): The artist  responsible for the album
            default artist name will be "Various Artists"
        tracks (list[Song]): A list of the songs on the album
    Methods:
        add_song: Used to add a new song to the album's tracklist
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist["Various Artists"]
        else:
            self.artist = artist

        self.tracks = []


    def add_song(self, song, position=None):
        """Adds a song to the track list
        Args:
            song (Song): A song to add
            position (Optional(int)): A song to be added to that position in the
                track list
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)

