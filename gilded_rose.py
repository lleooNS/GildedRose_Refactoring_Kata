# -*- coding: utf-8 -*-


max_quality = 50

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    # def update_quality(self):
    #     for item in self.items:
    #         if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
    #             if item.quality > 0:
    #                 if item.name != "Sulfuras, Hand of Ragnaros":
    #                     item.quality = item.quality - 1
    #         else:
    #             if item.quality < 50:
    #                 item.quality = item.quality + 1
    #                 if item.name == "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.sell_in < 11:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #                     if item.sell_in < 6:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #         if item.name != "Sulfuras, Hand of Ragnaros":
    #             item.sell_in = item.sell_in - 1
    #         if item.sell_in < 0:
    #             if item.name != "Aged Brie":
    #                 if item.name != "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.quality > 0:
    #                         if item.name != "Sulfuras, Hand of Ragnaros":
    #                             item.quality = item.quality - 1
    #                 else:
    #                     item.quality = item.quality - item.quality
    #             else:
    #                 if item.quality < 50:
    #                     item.quality = item.quality + 1


    def update_quality(self):

        

        for item in self.items:

            product = CreateClassProduct.create_class(item)
            product.update_item_quality()


            # self.update_item_quality(item)

    def update_item_quality(self, item):

        if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            if item.quality > 0:
                if item.name != "Sulfuras, Hand of Ragnaros":
                    item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)



class CommonProduct(object):

    def __init__(self, item):
        self.item = item

    def update_item_quality(self):

        if self.item.sell_in < 0 and self.item.quality > 0:
            self.item.quality -= 1

        if self.item.quality > 0:
            self.item.quality -= 1

        self.item.sell_in -= 1

class AgedBrieProduct(object):

    def __init__(self, item):
        self.item = item

    def update_item_quality(self):

        self.item.sell_in -= 1

        if self.item.quality < max_quality:
            self.item.quality += 1

class SulfurasProduct(object):

    def __init__(self, item):
        self.item = item

    def update_item_quality(self):
        pass

class BackstagePassesProduct(object):

    def __init__(self, item):
        self.item = item

    def update_item_quality(self):

        if self.item.quality < max_quality:

            self.item.quality += 1

            if self.item.sell_in < 11 and self.item.quality < max_quality:
                self.item.quality += 1
            if self.item.sell_in < 6 and self.item.quality < max_quality:
                self.item.quality += 1

        if self.item.sell_in < 0:
            self.item.quality = 0

        self.item.sell_in -= 1

class ConjuredProduct(object):

    def __init__(self, item):
        self.item = item

    def update_item_quality(self):

        if self.item.quality > 0:
            self.item.quality -= 1
            if self.item.quality > 0:
                self.item.quality -= 1

        self.item.sell_in -= 1

class CreateClassProduct(object):

    product_classes = {
        'Aged Brie': AgedBrieProduct,
        'Sulfuras, Hand of Ragnaros': SulfurasProduct,
        'Backstage passes to a TAFKAL80ETC concert': BackstagePassesProduct,
        'Conjured Mana Cake': ConjuredProduct
    }

    def __init__(self, item):
        self.item = item

    @classmethod
    def create_class(cls, item):
        if item.name in cls.product_classes:
            return cls.product_classes[item.name](item)

        return CommonProduct(item)

