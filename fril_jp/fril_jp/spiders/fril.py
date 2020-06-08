# -*- coding: utf-8 -*-
import scrapy


class FrilSpider(scrapy.Spider):
    name = 'fril'
    allowed_domains = ['fril.jp']
    start_urls = ['http://fril.jp/']

    def parse(self, response):
        print(response)
        pass
