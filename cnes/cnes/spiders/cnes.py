# -*- coding: utf-8 -*-

import re
import scrapy
import pandas as pd
from cnes_scrapy.items import CnesScrapyItem


class CnesSpider(scrapy.Spider):
    name = 'cnes'
    allowed_domains = ['cnes2.datasus.gov.br/']
    start_urls = ['http://cnes2.datasus.gov.br/Mod_Ind_Equipamento.asp?']
