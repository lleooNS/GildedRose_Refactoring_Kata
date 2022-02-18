# -*- coding: utf-8 -*-
import unittest

from src.gilded_rose.gilded_rose import Item, GildedRose
from tests.test_aged_brie import TestAgedBrie
from tests.test_backstage_passes import TestBackstagePasses
from tests.test_common import TestCommon
from tests.test_conjured import TestConjured
from tests.test_sulfuras import TestSulfuras


class GildedRoseTest(unittest.TestCase):

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_common(self):
        test_common = TestCommon()
        test_common.run_tests()

    def test_aged_brie(self):
        test_aged_brie = TestAgedBrie()
        test_aged_brie.run_tests()

    def test_sulfuras(self):
        test_sulfuras = TestSulfuras()
        test_sulfuras.run_tests()

    def test_backstage_passes(self):
        test_backstage_passes = TestBackstagePasses()
        test_backstage_passes.run_tests()

    def test_conjured(self):
        test_conjured = TestConjured()
        test_conjured.run_tests()


if __name__ == '__main__':
    unittest.main()
