# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_item()
        self.assertEqual(["Sulfuras"], all_items)

    def test_aged_brie_increases_in_quality(self):
        """ 'Aged Brie' actually increases in Quality the older it gets """
        item = Item("Aged Brie", 2, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertGreater(item.quality, 10, "Aged Brie should increase in quality")

    def test_backstage_passes_quality_drops_to_zero_after_concert(self):
        """ 'Backstage passes', like aged brie, increases in Quality as its SellIn value approaches;
Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
Quality drops to 0 after the concert """
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 0, "Backstage passes should have 0 quality after the concert")

    def test_conjured_items_degrade_twice_as_fast(self):
        """ 'Conjure'" items degrade in Quality twice as fast as normal items """
        item = Item("Conjured Mana Cake", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 8, "Conjured items should lose 2 quality per day")

    def test_syntax_error_attribute(self):
        """ Test accessing a non-existing attribute 'customer' """
        item = Item("Normal Item", 5, 10)
        gilded_rose = GildedRose([item])
        with self.assertRaises(AttributeError):
            _ = gilded_rose.customer  # This attribute does not exist


if __name__ == '__main__':
    unittest.main()
