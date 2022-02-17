
class AgedBrieProduct(object):

    def __init__(self, item):
        self.item = item

    def decrement_item_sell_in(self):
        self.item.sell_in -= 1

    def increment_item_quality(self):
        self.item.quality += 1

    def update_item_quality(self):

        from src.gilded_rose.gilded_rose import max_quality

        self.decrement_item_sell_in()

        if self.item.quality < max_quality:
            self.increment_item_quality()
