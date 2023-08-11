import json
import sys
from datetime import datetime
from xml.etree import ElementTree

import gpxpy
import gpxpy.gpx


def owntrack2gpx(input: dict) -> gpxpy.gpx.GPX:
    user = list(input.keys())[0]
    gpx = gpxpy.gpx.GPX()

    devices = input[user]

    first_device_name = list(devices.keys())[0]
    first_device = devices[first_device_name]

    gpx.time = datetime.utcnow()
    gpx.name = f"{user}-{first_device_name}"

    # Create first track in our GPX:
    gpx_track = gpxpy.gpx.GPXTrack(name=first_device_name)
    gpx.tracks.append(gpx_track)

    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)
    for point in first_device:
        p = gpxpy.gpx.GPXTrackPoint(
            latitude=point['lat'],
            longitude=point['lon'],
            elevation=point['alt'],
            time=datetime.fromisoformat(point['disptst']),
        )
        p.satellites = 0
        battery = f"<batterylevel>{point['batt']}</batterylevel>"
        p.extensions = [
            ElementTree.fromstring(f"<speed>{point['vel']/3.6}</speed>"),
            ElementTree.fromstring("<course>0.000</course>"),
            ElementTree.fromstring(f"<accuracy>{point['acc']}</accuracy>"),
            ElementTree.fromstring(battery),
            ElementTree.fromstring("<useragent>PhoneTrack/0.1.0</useragent>"),
        ]
        gpx_segment.points.append(p)

    return gpx


def main():
    i = sys.stdin.read()
    i = i.replace("'", '"')
    j = json.loads(i)
    o = owntrack2gpx(j).to_xml()
    print(o)


if __name__ == '__main__':
    main()
