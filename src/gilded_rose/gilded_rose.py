# -*- coding: utf-8 -*-
from src.products.aged_brie_product import AgedBrieProduct
from src.products.backstage_passes_product import BackstagePassesProduct
from src.products.common_product import CommonProduct
from src.products.conjured_product import ConjuredProduct
from src.products.sulfuras_product import SulfurasProduct

max_quality = 50


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
