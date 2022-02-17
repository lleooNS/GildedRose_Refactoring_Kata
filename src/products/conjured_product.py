
class ConjuredProduct(object):

    def __init__(self, item):
        self.item = item

    def decrement_item_quality(self):
        self.item.quality -= 1

    def decrement_item_sell_in(self):
        self.item.sell_in -= 1

    def update_item_quality(self):

        if self.item.quality > 0:
            self.decrement_item_quality()
            if self.item.quality > 0:
                self.decrement_item_quality()

        self.decrement_item_sell_in()
