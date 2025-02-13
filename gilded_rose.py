# -*- coding: utf-8 -*-
class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Skip Sulfuras entirely (no changes to quality or sell_in)
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue  # Skip Sulfuras processing

            # Handle Aged Brie
            if item.name == "Aged Brie":
                if item.quality < 50:
                    item.quality += 1

            # Handle Backstage passes to a TAFKAL80ETC concert
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in <= 0:
                    item.quality = 0  # Quality drops to 0 after the concert
                elif item.sell_in <= 5:
                    if item.quality < 50:
                        item.quality += 3  # Quality increases by 3 if there are 5 days or less
                elif item.sell_in <= 10:
                    if item.quality < 50:
                        item.quality += 2  # Quality increases by 2 if there are 10 days or less

            # Handle Conjured items (degrade twice as fast)
            elif "Conjured" in item.name:
                if item.quality > 0:
                    item.quality -= 2

            # Handle Normal items (degrade normally)
            else:
                if item.quality > 0:
                    item.quality -= 1

            # Decrease sell_in for all items except Sulfuras
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1

            # Quality changes for items after sell_in < 0
            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    if item.quality < 50:
                        item.quality += 1
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0  # Quality is zero after the concert
                elif item.quality > 0:
                    item.quality -= 1  # Normal items degrade by 1 more if past sell_in
