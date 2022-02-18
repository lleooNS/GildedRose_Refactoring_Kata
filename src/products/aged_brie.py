from configs.environments import max_quality
from src.products.product import Product


class AgedBrie(Product):

    def __init__(self, item):
        super().__init__(item)

    def update_item_quality(self):

        super().update_item_quality()
        super().increment_item_quality()

        if self.item.sell_in < 0 and self.item.quality < max_quality:
            self.item.quality += 1
