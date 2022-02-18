from configs.environments import max_quality


class Product(object):

    def __init__(self, item):
        self.item = item

    def decrement_item_sell_in(self):
        self.item.sell_in -= 1

    def decrement_item_quality(self):
        if self.item.quality > 0:
            self.item.quality -= 1

    def increment_item_quality(self):
        if self.item.quality < max_quality:
            self.item.quality += 1

    def update_item_quality(self):
        self.decrement_item_sell_in()
