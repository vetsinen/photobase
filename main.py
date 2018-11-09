import os, time
from stat import * # ST_SIZE etc

file = ".gitignore"

try:
    st = os.stat(file)
except IOError:
    print ("failed to get information about", file)
else:
    print(st)
    # print ("file size:", st[ST_SIZE])
    # print ("file modified:", time.asctime(time.localtime(st[ST_MTIME])))