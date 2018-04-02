# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

def filter_price(value):
    return value[-2]

class DinatonCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    default_imput_processor = TakeFirst()
    default_output_processor = Join()
    _ID_ = Field(output_processor=Join())
    _MAIN_CATEGORY_ = Field(output_processor=Join())
    _CATEGORY_ID_ = Field(output_processor=Join())
    _NAME_ = Field(output_processor=Join())
    _MODEL_ = Field(output_processor=TakeFirst())
    _SKU_ = Field(output_processor=Join())
    _EAN_ = Field(output_processor=Join())
    _JAN_ = Field(output_processor=Join())
    _ISBN_ = Field(output_processor=Join())
    _MPN_ = Field(output_processor=Join())
    _UPC_ = Field(output_processor=Join())
    _MANUFACTURER_ = Field(
        input_processor=TakeFirst(),
        output_processor=Join()
    )
    _SHIPPING_ = Field(output_processor=TakeFirst())
    _LOCATION_ = Field(output_processor=Join())
    _PRICE_ = Field()
    _POINTS_ = Field(output_processor=TakeFirst())
    _REWARD_POINTS_ = Field(output_processor=TakeFirst())
    _QUANTITY_ = Field(output_processor=TakeFirst())
    _STOCK_STATUS_ID_ = Field(output_processor=TakeFirst())
    _STOCK_STATUS_ = Field(output_processor=Join())
    _LENGTH_ =  Field(output_processor=TakeFirst())
    _WIDTH_ =  Field(output_processor=TakeFirst())
    _HEIGHT_ =  Field(output_processor=TakeFirst())
    _WEIGHT_ =  Field(output_processor=TakeFirst())
    _META_TITLE_ = Field(output_processor=Join())
    _META_H1_ = Field(output_processor=Join())
    _META_KEYWORDS_ = Field(output_processor=Join())
    _META_DESCRIPTION_ =Field(output_processor=Join())
    _DESCRIPTION_ = Field(output_processor=Join())
    _PRODUCT_TAG_ = Field(output_processor=TakeFirst())
    _IMAGE_ =Field(output_processor=Join())
    _IMAGE_URL_ = Field(output_processor=Join())
    _SORT_ORDER_ =  Field(output_processor=TakeFirst())
    _STATUS_ =Field(output_processor=TakeFirst())
    _SEO_KEYWORD_ = Field(output_processor=Join())
    _DISCOUNT_ = Field(output_processor=TakeFirst())
    _SPECIAL_ = Field(output_processor=TakeFirst())
    _OPTIONS_ = Field(output_processor=TakeFirst())
    _FILTERS_ = Field(output_processor=TakeFirst())
    _ATTRIBUTES_ = Field(output_processor=TakeFirst())
    _IMAGES_ = Field()
    _STORE_ID_ =  Field(output_processor=TakeFirst())
    _URL_ = Field(output_processor=Join())
    image_urls = Field()
    images = scrapy.Field()
