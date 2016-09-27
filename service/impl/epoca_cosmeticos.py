# coding: utf-8

import os
from ..crawlable import Crawlable 

class EpocaCosmeticos(Crawlable):
    
    def get_crawlable_name(self):
        return 'EpocaCosmeticos'

    def get_category_pages(self):
        #link_crawler([os.path.join(base_path, 'home.html'), os.path.join(base_path, 'categoria_1.html')], '.*produto.*.html$')
        return [os.path.join(base_path, 'home.html'), os.path.join(base_path, 'categoria_1.html')]

    def get_product_pages(self):
        return '.*/p$'
    
    def get_product_name(self):
        return '//div[@class="productName"]/text()'