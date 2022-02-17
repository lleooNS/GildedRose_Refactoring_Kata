# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_items(self):

        items = [
            Item("+5 Dexterity Vest", 10, 20),
            Item("+5 Dexterity Vest", -3, 0),
            Item("Aged Brie", 2, 0),
            Item("Elixir of the Mongoose", 5, 7),
            Item("Elixir of the Mongoose", -2, 10),
            Item("Sulfuras, Hand of Ragnaros", 0, 80),
            Item("Sulfuras, Hand of Ragnaros", -1, 80),
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 49),
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 49),
            Item("Backstage passes to a TAFKAL80ETC concert", -10, 33),
            Item("Conjured Mana Cake", 3, 6),
            Item("Conjured Mana Cake", 0, 1)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        values = [
            (9, 19), (-4, 0), (1, 1), (4, 6), (-3, 8), (0, 80), (-1, 80),
            (14, 21), (9, 50), (4, 50), (-11, 0), (2, 4), (-1, 0)
        ]

        for i, item in enumerate(items):

            self.assertEqual(values[i][0], item.sell_in)
            self.assertEqual(values[i][1], item.quality)



        
if __name__ == '__main__':
    unittest.main()
