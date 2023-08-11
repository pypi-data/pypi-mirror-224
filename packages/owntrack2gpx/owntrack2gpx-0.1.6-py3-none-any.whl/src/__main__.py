import json
import sys

from .convert import owntrack2gpx

if __name__ == '__main__':
    i = sys.stdin.read()
    i = i.replace("'", '"')
    j = json.loads(i)
    o = owntrack2gpx(j).to_xml()
    print(o)
