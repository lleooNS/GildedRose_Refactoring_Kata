from src.products.product import Product


class Conjured(Product):

    def __init__(self, item):
        super().__init__(item)

    def update_item_quality(self):
        super().update_item_quality()
        super().decrement_item_quality()
        super().decrement_item_quality()

        if self.item.sell_in < 0:
            super().decrement_item_quality()
            super().decrement_item_quality()
