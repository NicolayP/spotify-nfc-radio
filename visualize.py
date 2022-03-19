
# shows acoustic features for tracks for the given artist

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False

if len(sys.argv) > 1:
    artist_name = ' '.join(sys.argv[1:])
else:
    artist_name = 'weezer'

tid = 'spotify:track:6gdLoMygLsgktydTQ71b15'


start = time.time()
analysis = sp.audio_analysis(tid)
delta = time.time() - start
print(analysis)
#print(json.dumps(analysis, indent=4))
print("analysis retrieved in %.2f seconds" % (delta,))

'''
start = time.time()
features = sp.audio_features(tid)
delta = time.time() - start

for feature in features:
    print(json.dumps(feature, indent=4))
    print()
    analysis = sp._get(feature['analysis_url'])
    print(json.dumps(analysis, indent=4))
    print()
print("features retrieved in %.2f seconds" % (delta,))
'''