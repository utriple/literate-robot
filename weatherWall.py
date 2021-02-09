#! /usr/bin/python3 
#
# wallpaper.py 
# 
# Load the actual isobaric chart of europe from the dwd
# and set it as the desktop wallpaper
# (works with debian / raspbian, testet with lxde window manager )
#
# chmod +x <File>    don't forget !
#

import os
import requests
import time

# import sys

### internal consts ###
chunk_size = 100000

cmdChangeWallpaper = 'pcmanfm -w --set-wallpaper=%s'

### const ###

# isobaric chart
webAddress = 'https://www.dwd.de/DWD/wetter/wv_spez/hobbymet/wetterkarten/bwk_bodendruck_na_ana.png'
filename = 'bwk_bodendruck_na_ana.png'

# north sea temperature
# webAddress = 'https://www.dwd.de/DWD/wetter/wv_spez/hobbymet/wetterkarten/ico_wassertemp_na_ana.png'
# filename = 'ico_wassertemp_na_ana.png';

fname = '~/weatherWallpapers'

### main ###

foldername = os.path.expanduser(fname)

if not os.path.exists(foldername):
    print( 'folder %s created !' % foldername )
    x = os.mkdir(foldername)

filepath = os.path.join( foldername, time.strftime( '%y%m%d-', time.localtime() ) + filename )

if( os.path.exists( filepath ) ):
    print( 'wallpaper just downloaded !' )
    print( '(%s)' % filepath )
    exit()

print( 'Downloading %s...' % webAddress )
res = requests.get( webAddress )
res.raise_for_status()

webPageFile = open( filepath, 'wb' )

print( 'Writing %s...' % filepath )
for chunk in res.iter_content( chunk_size ):
    webPageFile.write( chunk )

webPageFile.close

print( 'Changing wallpaper %s...' % filepath )
os.system( cmdChangeWallpaper % filepath )
