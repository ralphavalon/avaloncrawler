# coding: utf-8

from ..crawlable import Crawlable 

class EpocaCosmeticos(Crawlable):
    def get_category_page(self):
        return 'category'

    def get_product_page(self):
        return 'product'
    
    def get_product_name(self):
        return 'name'

    def get_product_title(self):
        return 'title'

    def get_product_url(self):
        return 'url'