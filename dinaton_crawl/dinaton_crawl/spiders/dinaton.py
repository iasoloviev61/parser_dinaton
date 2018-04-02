# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from dinaton_crawl.items import DinatonCrawlItem
from scrapy.loader.processors import MapCompose, Join

# import json
# from transliterate import translit, get_available_language_codes

# category_file = open('../output/category.json',  encoding='utf8').read()
# category_data = json.loads(category_file)
product_array = []
# TODO занчение должно браться из последнего значегия экспорта магазина
MODEL_NUMBER = 5000
brand_no_change_price = ["yamaha", "casio", "roland", "boss", "korg"]

# def category(arr, value):
#     category_id = [str(17000)]
#     for index in arr:
#         if value in arr[index]:
#             category_id = [str(arr[index][0]), str(index)]
#         else:
#             continue
#     return category_id


class BasicSpider(scrapy.Spider):
    name = 'basic'
    start_urls = ['https://dynatone.ru/opt/getfile.php?fn=Product&ft=XML&pr=all&i=4876&d=1424984400']

    def parse(self, response):
        for href in response.xpath('/yml_catalog/shop/offers/offer/url/text()').extract()[0:10]:
            yield response.follow(href, self.parse_product)


    def parse_product(self, response):
        global MODEL_NUMBER
        image = response.xpath(
            '/html/body/span/table[1]//tr/td[3]//img[contains(@src, "/images/base/arm")]/@src').extract()
        l = ItemLoader(item=DinatonCrawlItem(), response=response)
        l.add_value('_ID_', '')
        l.add_value('_MAIN_CATEGORY_', '')
        l.add_css('_CATEGORY_ID_', 'div.smaller a:nth-last-child(2)')
        l.add_xpath('_NAME_', '/html/body/span/table[1]//tr/td[3]/table[1]//tr/td[2]/h1/span/text()')
        l.add_value('_MODEL_', MODEL_NUMBER)
        l.add_xpath('_SKU_', '/html/body/span/table[1]//tr/td[3]/table[1]//tr/td[1]/table//tr[1]/td[1]/b/text()')
        l.add_value('_EAN_', '')
        l.add_value('_JAN_', '')
        l.add_value('_ISBN_', '')
        l.add_value('_MPN_', '')
        l.add_value('_UPC_', '')
        l.add_xpath('_MANUFACTURER_', '/html/body/span/table[1]//tr/td[3]/a[1]/font/b/text()')
        l.add_value('_SHIPPING_', 0)
        l.add_value('_LOCATION_', 'Динатон')
        l.add_xpath('_PRICE_', '/html/body/span/table[1]//tr/td[3]/table[1]//tr/td[1]/table//tr[1]/td[1]/h1/span/text()')
        l.add_value('_POINTS_', 0)
        l.add_value('_REWARD_POINTS_', '')
        l.add_value('_QUANTITY_', 10)
        l.add_value('_STOCK_STATUS_ID_', 7)
        l.add_value('_STOCK_STATUS_', 'В наличии')
        l.add_value('_LENGTH_', 0)
        l.add_value('_WIDTH_', 0)
        l.add_value('_HEIGHT_', 0)
        l.add_value('_WEIGHT_', 0)
        l.add_xpath('_META_TITLE_', '/html/body/span/table[1]//tr/td[3]/table[1]//tr/td[2]/h1/span/text()')
        l.add_xpath('_META_H1_', '/html/body/span/table[1]//tr/td[3]/table[1]//tr/td[2]/h1/span/text()')
        l.add_xpath('_META_KEYWORDS_', '/html/body/span/table[1]//tr/td[3]/table[1]//tr/td[2]/h1/span/text()')
        l.add_xpath('_META_DESCRIPTION_', '/html/body/span/table[1]//tr/td[3]/table[1]//tr/td[2]/h1/span/text()')
        l.add_xpath('_DESCRIPTION_', '/html/body/span/table[1]//tr/td[3]/table[2]/tr/td/p')
        l.add_xpath('_DESCRIPTION_', '/html/body/span/table[1]//tr/td[3]/table[2]//tr/td//li')
        l.add_value('_PRODUCT_TAG_', '')
        # l.add_value('_IMAGE_')
        l.add_value('_SORT_ORDER_', 100)
        l.add_value('_STATUS_', 1)
        l.add_xpath('_SEO_KEYWORD_', '/html/body/span/table[1]//tr/td[3]/table[1]//tr/td[2]/h1/span/text()')
        l.add_value('_DISCOUNT_', '')
        l.add_value('_SPECIAL_', '')
        l.add_value('_OPTIONS_', '')
        l.add_value('_FILTERS_', '')
        l.add_value('_ATTRIBUTES_', '')
        # l.add_value('_IMAGES_', self.url_join(image, response))
        l.add_value('_STORE_ID_', 0)
        l.add_value('_URL_', '')
        # l.add_value('image_urls', self.url_join(image, response))

        MODEL_NUMBER = MODEL_NUMBER + 1
        return l.load_item()
    def url_join(self, urls, response):
        joined_urls = []
        for url in urls:
            joined_urls.append(response.urljoin(url))
        return joined_urls
        # category_id = category(catalog, categorys)
        # sku = response.xpath('/html/body/span/table[1]//tr/td[3]/table[1]//tr/td[1]/table//tr[1]/td[1]/b/text()').extract()
        #
        # title = response.xpath(
        #     '/html/body/span/table[1]//tr/td[3]/table[1]//tr/td[2]/h1/span/text()').extract()
        # price = response.xpath('/html/body/span/table[1]//tr/td[3]/table[1]//tr/td[1]/table//tr[1]/td[1]/h1/span/text()').extract()
        # description = response.xpath(
        #     '/html/body/span/table[1]//tr/td[3]/table[2]/tr/td/p').extract()
        # options = response.xpath('/html/body/span/table[1]//tr/td[3]/table[2]//tr/td//li').extract()
        # image = response.xpath(
        #     '/html/body/span/table[1]//tr/td[3]//img[contains(@src, "/images/base/arm")]/@src').extract()
        # item = DinatonCrawlItem()
        # item['_ID_'] = ""
        # item['_MAIN_CATEGORY_'] = ""
        # item['_CATEGORY_ID_'] = response.xpath('//div[@class="smaller"]//a/text()').extract()[-2]
        # item['_NAME_'] = title
        # item['_MODEL_'] = ""
        # item['_SKU_'] = sku
        # item['_EAN_'] = ""
        # item['_JAN_'] = ""
        # item['_ISBN_'] = ""
        # item['_MPN_'] = ""
        # item['_UPC_'] = ""
        # item['_MANUFACTURER_'] = response.xpath('/html/body/span/table[1]//tr/td[3]/a[1]/font/b/text()').extract()
        # item['_SHIPPING_'] = 0
        # item['_LOCATION_'] = "Динатон"
        # item['_PRICE_'] = price
        # item['_POINTS_'] = 0
        # item['_REWARD_POINTS_'] = ""
        # item['_QUANTITY_'] = 10
        # item['_STOCK_STATUS_ID_'] = 7
        # item['_STOCK_STATUS_'] = "В наличии"
        # item['_LENGTH_'] = 0
        # item['_WIDTH_'] = 0
        # item['_HEIGHT_'] = 0
        # item['_WEIGHT_'] = 0
        # item['_META_TITLE_'] = ''.join(title) + " в интернет магазине Евтерпа доставка по России цена, магазин Москва"
        # item['_META_H1_'] = title
        # item['_META_KEYWORDS_'] = "0"
        # item['_META_DESCRIPTION_'] ="0"
        # item['_DESCRIPTION_'] = description + options
        # item['_PRODUCT_TAG_'] = ""
        # item['_IMAGE_'] = image
        # item['_SORT_ORDER_'] = 100
        # item['_STATUS_'] = 1
        # item['_SEO_KEYWORD_'] = ""
        # item['_DISCOUNT_'] = ""
        # item['_SPECIAL_'] = ""
        # item['_OPTIONS_'] = ""
        # item['_FILTERS_'] = ""
        # item['_ATTRIBUTES_'] = ""
        # item['_IMAGES_'] = ""
        # item['_STORE_ID_'] = 0
        # item['_URL_'] = ""
        # item['image_urls'] = self.url_join(image, response)
        # return item

    # def url_join(self, urls, response):
    #     joined_urls = []
    #     for url in urls:
    #         joined_urls.append(response.urljoin(url))
    #
    #     return joined_urls