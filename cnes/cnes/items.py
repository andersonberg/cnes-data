# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Field, Item


class CityItem(Item):
    cidade = Field()
    estado = Field()
    equipamentos = Field()
    url = Field()


class EquipmentItem(Item):
    equipamento = Field()
    existentes = Field()
    emUso = Field()
    existentesSUS = Field()
    emUsoSUS = Field()
