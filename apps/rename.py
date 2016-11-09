import glob
import re
import os

files = glob.glob('ap[0-9]*')
for file in files:
    print(file)
    matches = re.compile('^ap([0-9]*)').search(file)
    if matches:
        print(matches)
        num = matches.group(1)
        # os.rename(file, 'app' + '%02d' % int(num))
        os.rename(file, 'app' + num.zfill(2))

