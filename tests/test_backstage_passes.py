
from src.gilded_rose.gilded_rose import Item
from tests.basic_test import BasicTest


class TestBackstagePasses(BasicTest):

    def test_never_negative_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 38)]
        super().common_test(items, -90, 0, 100)

    def test_quality_greater_than_ten_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        super().common_test(items, 14, 21, 1)

    def test_quality_less_than_ten_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 40)]
        super().common_test(items, 9, 42, 1)

    def test_quality_less_than_five_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 45)]
        super().common_test(items, 4, 48, 1)

    def test_quality_never_higher_than_fifty(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        super().common_test(items, 4, 50, 1)

    def run_tests(self):
        self.test_never_negative_quality()
        self.test_quality_greater_than_ten_days()
        self.test_quality_less_than_ten_days()
        self.test_quality_less_than_five_days()
        self.test_quality_never_higher_than_fifty()
