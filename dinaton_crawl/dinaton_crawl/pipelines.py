# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import csv
from transliterate import translit, get_available_language_codes

with open('./output/product_name.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

your_list = your_list[1:]
list_name = []
for item in your_list:
    item_clean = ''.join(item).split(";")[-1][1:-1]
    list_name.append(item_clean)

class DinatonCrawlPipeline(object):
    def process_item(self, item, spider):

        return item

class DropDupName(object):
    def process_item(self, item, spider):
        if item['_NAME_'] in list_name:
            print("duplicate find")
            raise DropItem("Duplicate item found: %s" % item)
        else:
            return item

class TranslitSeoKeyWord(object):
    def process_item(self, item, spider):
        item['_SEO_KEYWORD_'] = translit(item['_SEO_KEYWORD_'], 'ru', reversed=True)\
            .replace(' ', '-')\
            .replace('/', '-')\
            .replace('.', '')\
            .replace(',', '')\
            .replace('\'', '')
        item['_META_TITLE_'] =  "Купить " + item['_META_TITLE_'] + " в интернет магазине Евтерпа доставка по России цена, магазин Москва"
        item['_META_KEYWORDS_'] =  "Купить " + item['_META_KEYWORDS_'] + " в интернет магазине Евтерпа доставка по России цена, магазин Москва"
        item['_META_DESCRIPTION_'] = item['_META_DESCRIPTION_'] + " по лучшей цене заходите у нас отличный выбор " + item['_META_DESCRIPTION_'] + " только оригинал бесплатная доставка по Москве и России."
        return item

# class PricePipeline(object):
#     def process_item(self, item, spider):
#         brand_no_change_price = ["yamaha", "casio", "roland", "boss", "korg"]
#         if len(item['_PRICE_']) > 0:
#             item['_PRICE_'] = item['_PRICE_'][0]
#             if item['_PRICE_'] == 0 or item['_PRICE_'] == None:
#                 item['_PRICE_'] = 0
#                 return item
#             else:
#                 item['_PRICE_'] = int(item['_PRICE_'].replace(' ', ''))
#                 if item['_MANUFACTURER_'].lower() in brand_no_change_price:
#                     return item
#                 else:
#                     item['_PRICE_'] = int(item['_PRICE_'] - (item['_PRICE_'] * 5 / 100))
#                     return item
#         else:
#             if item['_MANUFACTURER_'].lower() in brand_no_change_price:
#                 item['_PRICE_'] = 0
#                 return item

# class MyImagesPipeline(ImagesPipeline):
#
#     def get_media_requests(self, item, info):
#         for image_url in item['_IMAGES_']:
#             yield scrapy.Request(image_url)
#
#     def item_completed(self, results, item, info):
#         image_paths = [x['path'] for ok, x in results if ok]
#         if not image_paths:
#             raise DropItem("Item contains no images")
#         item['_IMAGE_'] = image_paths
#         return item
# class ClearDataPipeline(object):
#     def process_item(self, item, spider):
#         item['_IMAGES_'] = ""
#         item['_IMAGE_'] = ''.join(item['_IMAGE_']).replace('full/', '')
#         return item
class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['_NAME_'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['_NAME_'])
            return item