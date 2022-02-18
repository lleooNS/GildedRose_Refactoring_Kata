
from src.gilded_rose.gilded_rose import Item
from tests.basic_test import BasicTest


class TestSulfuras(BasicTest):

    def test_final_of_the_day(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        super().common_test(items, -1, 80, 1000)

    def run_tests(self):
        self.test_final_of_the_day()
