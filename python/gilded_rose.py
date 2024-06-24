# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
# function to update quality of items 
    def update_quality(self):
       for item in self.items:
        if item.name == "Sulfuras, Hand of Ragnaros":
            continue  #Ensuring Sulfuras quality value never changes
        elif "Aged Brie" in item.name:
            item.quality += 1
        elif "Backstage passes" in item.name:
            if item.sell_in <= 0:
                item.quality = 0
            elif item.sell_in <= 5:
                item.quality += 3
            elif item.sell_in <= 10:
                item.quality += 2
            else:
                item.quality += 1
        elif "Conjured" in item.name:
            item.quality /= 2
        else:
            item.quality -= 1

        # Ensure quality limits are respected
        if item.quality > 50:
            item.quality = 50
        elif item.quality < 0:
            item.quality = 0

        # Decrease rate sell_in for all items (except Sulfuras)
        item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
