# coding: utf-8

import os
from ..crawlable import Crawlable 

class EpocaCosmeticos(Crawlable):
    
    def get_crawlable_name(self):
        return 'EpocaCosmeticos'

    def get_category_pages(self):
        return '//div[@class="menu"]//a/@href'

    def get_product_pages(self):
        return '.*/p$'

    def get_home_page(self):
        return 'http://www.epocacosmeticos.com.br/'
    
    def get_product_name(self):
        return '//div[@class="productName"]/text()'