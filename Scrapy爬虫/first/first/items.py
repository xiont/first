# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#class ZoneItem(scrapy.Item):
    #content=scrapy.Field()
    #url=scrapy.Field()
    
class TaobaoItem(scrapy.Item):
    content=scrapy.Field()
    #url=scrapy.Field()