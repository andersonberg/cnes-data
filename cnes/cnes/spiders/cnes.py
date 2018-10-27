# -*- coding: utf-8 -*-

import re
import scrapy
# import pandas as pd
from urllib.parse import unquote, urljoin
from cnes.items import CnesItem


class CnesSpider(scrapy.Spider):
    name = 'cnes'
    allowed_domains = ['cnes2.datasus.gov.br']
    start_urls = ['http://cnes2.datasus.gov.br/Mod_Ind_Equipamento.asp']
    start_urls = []
    base_url = 'http://cnes2.datasus.gov.br/Mod_Ind_Equipamento.asp'

    br_states = {
        'ACRE': '12',
        'ALAGOAS': '27',
    }

    def start_requests(self):
        for state in self.br_states.values():
            if state == '00' or not state:
                continue
            state_url = unquote(urljoin(self.base_url, f'?VEstado={state}'))
            yield scrapy.Request(
                state_url,
                callback=self.parse_state,
                meta={
                    'state_code': state,
                },
            )

    def parse_state(self, response):
        state = response.meta['state_code']
        cities = response.css("select[name='ComboMunicipio'] > option ::attr(value)").extract()
        for city in cities:
            if city:
                city_url = unquote(f'http://cnes2.datasus.gov.br/Mod_Ind_Equipamento.asp?VEstado={state}&VMun={city}')
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
        # for sel in table.xpath('.//tr'):
        #     line = sel.xpath('td/font/text()').extract()
        #     print(line)
        return
