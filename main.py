import os, time
from stat import *  # ST_SIZE etc
import json

default = []
bytes = 0
for entry in os.scandir('photos/'):
    info = entry.stat()
    rec = {'name': entry.name, "modified": int(info.st_mtime), 'size': info.st_size, 'url':
        'https://vetsinen.github.io/photobase/photos/' + entry.name}
    bytes += info.st_size
    default.append(rec)

# print(json.dumps(default))

bysizea = sorted(default, key=lambda k: k['size'])
meta = {'bytes': bytes,'default':default, 'bysize': sorted(default, key=lambda k: k['size'])
    , 'byfilename': sorted(default, key=lambda k: k['name'])
    , 'bynamelength': sorted(default, key=lambda k: len(k['name']))}
with open('base.json', 'w') as f:
    f.write(json.dumps(meta))
