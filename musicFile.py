import eyed3
import requests

# testing music retrieval locally
# eventually this will be done with API info from the backend server

class MusicFileInfo:
    def __init__(self):
        # filename will hold file name and path to music file
        self.musfile = None
        # list to hold music files that will be added
        self.mstruct = []
        # variable to hold number of files that are passed
        # should be all the music files on the server
        self.numfiles = 0


    def getMusic(self):
        # we will get music files from API
        resp = requests.get('http://127.0.0.1:8000/api/song/')
        if resp.status_code != 200:
            # there was a mistake of somesort
            raise ApiError('Get /song/ {} '.format(resp.status_code) )
        for item in resp.json():
            # add to list structure which will be returned
            self.mstruct.append(item)

            # quick test to make sure I am getting correct items
            # test to see if we get proper components
            #print('{} {} {} {}  '.format(item['id'], item['song'], item['album'], item['musicfile'] ))
        # return both
        self.numfiles = len(self.mstruct)

        return self.mstruct, self.numfiles


    def getInfo(self):
        # incase Music file has no info use this to quickly get the info
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

    def setFilename(self, fname):
        self.musfile = fname


'''
# test to see if eyed3 works
# path to file
filename = "music/01 Coke Boyz ft. Meek Mill (Prod by Black Metaphor, Rick Steel, Young Chop).mp3"
c = MusicFileInfo(filename)
info = c.getInfo()
f = c.getFilename()
c.getMusic()
print(f)
print(info)
'''
