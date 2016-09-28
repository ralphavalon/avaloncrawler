# coding: utf-8

import os
from unittest import TestCase
from crawling.crawler import Crawler
from model.page import Page
from service.impl.epoca_cosmeticos import EpocaCosmeticos

class CrawlerUnitTest(TestCase):

    def test_get_product(self):
        crawler = Crawler()
        base_path = os.path.abspath('.') + os.sep + 'tests'
        file_base_path = 'file:///' + base_path
        link = os.path.join(file_base_path, 'produto_1.html')
        epoca = EpocaCosmeticos()
        print epoca.get_product_pages()
        product = Page(EpocaCosmeticos(), link).get_product()
        self.assertEquals('Produto 1', product.name)
        self.assertEquals('Titulo do Produto 1', product.title)
        self.assertEquals(link, product.url)