
from src.gilded_rose.gilded_rose import Item
from tests.basic_test import BasicTest


class TestAgedBrie(BasicTest):

    def test_product_expired(self):
        items = [Item("Aged Brie", -1, 26)]
        super().common_test(items, -2, 28, 1)

    def test_never_negative_quality(self):
        items = [Item("Aged Brie", 10, 38)]
        super().common_test(items, -90, 50, 100)

    def run_tests(self):
        self.test_product_expired()
        self.test_never_negative_quality()
