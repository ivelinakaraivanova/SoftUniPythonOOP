class Album:
    def __init__(self, name: str, songs=None):
        self.name = name
        if songs is None:
            self.songs = []
        elif not isinstance(songs, list):
            self.songs = [songs]
        else:
            self.songs = songs
        self.published = False

    def add_song(self, song):
        if song in self.songs:
            return "Song is already in the album."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        songs_names = [s.name for s in self.songs]
        if song_name not in songs_names:
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        song = [s for s in self.songs if s.name == song_name][0]
        self.songs.remove(song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for s in self.songs:
            result += f'== {s.get_info()}\n'
        return result
