from configs.environments import max_quality
from src.products.product import Product


class BackstagePasses(Product):

    def __init__(self, item):
        super().__init__(item)

    def update_item_quality(self):

        # ***** Decrease before or after?
        # super().update_item_quality()

        super().increment_item_quality()

        if self.item.sell_in < 11 and self.item.quality < max_quality:
            self.item.quality += 1
        if self.item.sell_in < 6 and self.item.quality < max_quality:
            self.item.quality += 1

        # ***** Decrease before or after?
        super().update_item_quality()

        if self.item.sell_in < 0:
            self.item.quality = 0
