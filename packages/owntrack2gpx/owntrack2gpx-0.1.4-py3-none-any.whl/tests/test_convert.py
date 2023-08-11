import json
import unittest

import freezegun

from src import owntrack2gpx


class OwnTrack2GPX(unittest.TestCase):
    @freezegun.freeze_time("2023-07-26T13:20:25Z")
    def test_owntrack2gpx_integration(self):
        with open('./tests/data.json', 'r') as data:
            with open('./tests/expected.gpx', 'r') as expected:
                j = json.load(data)
                o = owntrack2gpx(j).to_xml().splitlines()
                er = expected.read().splitlines()
                self.assertEqual(o[2:], er[2:])


if __name__ == '__main__':
    unittest.main()
