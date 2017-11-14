import eyed3

# testing music retrieval locally
# eventually this will be done with API info from the backend server

class MusicFileInfo:
    def __init__(self, filename):
        # filename will hold file name and path to music file
        self.musfile = filename


    def getInfo(self):
        audiofile = eyed3.load(self.musfile)
        # create dictionary with info we need
        info = {"artist": audiofile.tag.artist,
                "album": audiofile.tag.album ,
                "song_title": audiofile.tag.title,
                "track_num": audiofile.tag.track_num,
                "genre": audiofile.tag.genre
                }
        return info

    def getFilename(self):
        return self.musfile


'''
# test to see if eyed3 works
# path to file
filename = "music/01 Coke Boyz ft. Meek Mill (Prod by Black Metaphor, Rick Steel, Young Chop).mp3"
c = MusicFileInfo(filename)
info = c.getInfo()
f = c.getFilename()
print(f)
print(info)
'''
