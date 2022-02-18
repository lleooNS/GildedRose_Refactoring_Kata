import unittest

from src.gilded_rose.gilded_rose import GildedRose


class BasicTest(unittest.TestCase):

    def common_test(self, items, final_sell_in, final_quality, number_of_days):

        gilded_rose = GildedRose(items)

        for u in range(number_of_days):
            gilded_rose.update_quality()

        self.assertEqual(final_sell_in, items[0].sell_in)
        self.assertEqual(final_quality, items[0].quality)
