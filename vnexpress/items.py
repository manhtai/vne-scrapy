# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VnexpressItem(scrapy.Item):
    post_date = scrapy.Field()
    title = scrapy.Field()
    short_intro = scrapy.Field()
    long_content = scrapy.Field()
    comments = scrapy.Field()
    tags = scrapy.Field()
