
from src.gilded_rose.gilded_rose import Item
from tests.basic_test import BasicTest


class TestCommon(BasicTest):

    def test_product_expired(self):
        items = [Item("+5 Dexterity Vest", -1, 17)]
        super().common_test(items, -2, 15, 1)

    def test_never_negative_quality(self):
        items = [Item("Elixir of the Mongoose", 10, 49)]
        super().common_test(items, -90, 0, 100)

    def test_final_of_the_day(self):
        items = [Item("Elixir of the Mongoose", 22, 39)]
        super().common_test(items, 21, 38, 1)

    def run_tests(self):
        self.test_product_expired()
        self.test_never_negative_quality()
        self.test_final_of_the_day()
