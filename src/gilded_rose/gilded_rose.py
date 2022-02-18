# -*- coding: utf-8 -*-
from src.products.aged_brie import AgedBrie
from src.products.backstage_passes import BackstagePasses
from src.products.common import Common
from src.products.conjured import Conjured
from src.products.sulfuras import Sulfuras


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:

            product = CreateClassProduct.create_class(item)
            product.update_item_quality()


class Item:

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class CreateClassProduct(object):

    product_classes = {
        'Aged Brie': AgedBrie,
        'Sulfuras, Hand of Ragnaros': Sulfuras,
        'Backstage passes to a TAFKAL80ETC concert': BackstagePasses,
        'Conjured Mana Cake': Conjured
    }

    def __init__(self, item):
        self.item = item

    @classmethod
    def create_class(cls, item):

        if item.name in cls.product_classes:

            return cls.product_classes[item.name](item)

        return Common(item)
