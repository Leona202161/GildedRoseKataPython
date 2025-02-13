# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# Quality Update Strategy Interface
class QualityUpdateStrategy(ABC):
    @abstractmethod
    def update_quality(self, item):
        pass


# Concrete Strategy for Sulfuras (no change in quality)
class SulfurasStrategy(QualityUpdateStrategy):
    def update_quality(self, item):
        pass


# Concrete Strategy for Aged Brie (increases in quality)
class AgedBrieStrategy(QualityUpdateStrategy):
    def update_quality(self, item):
        if item.quality < 50:
            item.quality += 1


# Concrete Strategy for Backstage Passes (quality increases as sell_in decreases)
class BackstagePassesStrategy(QualityUpdateStrategy):
    def update_quality(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            if item.quality < 50:
                item.quality += 3
        elif item.sell_in <= 10:
            if item.quality < 50:
                item.quality += 2
        else:
            if item.quality > 0:
                item.quality -= 1


# Concrete Strategy for Conjured Items (degrade twice as fast)
class ConjuredItemStrategy(QualityUpdateStrategy):
    def update_quality(self, item):
        if item.quality > 1:  # Ensure the item does not go below 0
            item.quality -= 2
        else:
            item.quality = 0


# Concrete Strategy for Normal Items (degrade normally)
class NormalItemStrategy(QualityUpdateStrategy):
    def update_quality(self, item):
        if item.quality > 0:
            item.quality -= 1


class GildedRose(object):
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Skip Sulfuras entirely (no changes to quality or sell_in)
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue  # Skip Sulfuras processing

            # Call strategy based on item type
            if "Conjured" in item.name:
                conjured_item_strategy = ConjuredItemStrategy()
                conjured_item_strategy.update_quality(item)
            elif item.name == "Aged Brie":
                aged_brie_strategy = AgedBrieStrategy()
                aged_brie_strategy.update_quality(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                backstage_passes_strategy = BackstagePassesStrategy()
                backstage_passes_strategy.update_quality(item)
            else:
                normal_item_strategy = NormalItemStrategy()
                normal_item_strategy.update_quality(item)

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
