# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnesItem(scrapy.Item):
    cidade = scrapy.Field()
    equipamento = scrapy.Field()
    existentes = scrapy.Field()
    emUso = scrapy.Field()
    existentesSUS = scrapy.Field()
    emUsoSUS = scrapy.Field()
