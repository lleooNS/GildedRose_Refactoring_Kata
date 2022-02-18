
from src.gilded_rose.gilded_rose import Item
from tests.basic_test import BasicTest


class TestConjured(BasicTest):

    def test_product_expired(self):
        items = [Item("Conjured Mana Cake", -1, 26)]
        super().common_test(items, -2, 22, 1)

    def test_never_negative_quality(self):
        items = [Item("Conjured Mana Cake", 10, 31)]
        super().common_test(items, -90, 0, 100)

    def test_final_of_the_day(self):
        items = [Item("Conjured Mana Cake", 20, 19)]
        super().common_test(items, 19, 17, 1)

    def run_tests(self):
        self.test_product_expired()
        self.test_never_negative_quality()
        self.test_final_of_the_day()
