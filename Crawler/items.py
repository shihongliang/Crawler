# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
import scrapy

class UserItem(Item):
    id = Field()
    url_token = Field()
    type = Field()
    name = Field()
    url = Field()
    headline = Field()
    edu_member_tag = Field()  #type, member_tag
    gender = Field()   # 0 male 1 female -1 unsure
    badge = Field()

class DoubanItem(Item):
    url = Field() #href url
    name = Field() # name
    location = Field() #pl


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
