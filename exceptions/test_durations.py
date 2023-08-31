import unittest
import os
import main


csv_directory = "/Users/maverick/PycharmProjects/Game of Thrones Investigating"
os.chdir(csv_directory)


class TestDurations(unittest.TestCase):

    def test_season_1(self):
        season_1_duration = main.durations_sum[0]
        self.assertEqual(season_1_duration, 567)

    def test_season_2(self):
        season_2_duration = main.durations_sum[1]
        self.assertEqual(season_2_duration, 549)

    def test_season_3(self):
        season_3_duration = main.durations_sum[2]
        self.assertEqual(season_3_duration, 558)

    def test_season_4(self):
        season_4_duration = main.durations_sum[3]
        self.assertEqual(season_4_duration, 545)

    def test_season_5(self):
        season_5_duration = main.durations_sum[4]
        self.assertEqual(season_5_duration, 563)

    def test_season_6(self):
        season_6_duration = main.durations_sum[5]
        self.assertEqual(season_6_duration, 562)

    def test_season_7(self):
        season_7_duration = main.durations_sum[6]
        self.assertEqual(season_7_duration, 440)

    def test_season_8(self):
        season_8_duration = main.durations_sum[7]
        self.assertEqual(season_8_duration, 430)


if __name__ == "__main__":
    unittest.main()