# -*- coding: utf-8 -*-

import re
import scrapy
# import pandas as pd
from cnes.items import CnesItem


class CnesSpider(scrapy.Spider):
    name = 'cnes'
    allowed_domains = ['cnes2.datasus.gov.br/']
    start_urls = ['http://cnes2.datasus.gov.br/Mod_Ind_Equipamento.asp']

    def parse(self, response):
        for state in response.css(
                "select[name='ComboEstado'] > option ::attr(value)").extract():
            if state == '00' or not state:
                continue
            state_url = f'http://cnes2.datasus.gov.br/Mod_Ind_Equipamento.asp?VEstado={state}'
            yield scrapy.Request(
                state_url,
                callback=self.parse_state,
                meta={
                    'state_code': state,
                },
                dont_filter=True
            )

    def parse_state(self, response):
        state = response.meta['state_code']
        for city in response.css(
                "select[name='ComboMunicipio'] > option ::attr(value)").extract():
            if not city:
                continue
            city_url = f'http://cnes2.datasus.gov.br/Mod_Ind_Equipamento.asp?VEstado={state}&VMun={city}'
            yield scrapy.Request(
                city_url,
                callback=self.parse_city,
                meta={
                    'state_code': state,
                    'city_code': city,
                },
            )

    def parse_city(self, response):
        table = response.xpath('//table[@border="1"]')
        for sel in table.xpath('.//tr'):
            line = sel.xpath('td/font/text()').extract()
            print(line)
