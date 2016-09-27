# coding: utf-8

from unittest import TestCase
from crawling.crawler import Crawler
from service.impl.epoca_cosmeticos import EpocaCosmeticos

class CrawlerUnitTest(TestCase):

    def test_get_product(self):
        crawler = Crawler()
        html_response = '<div class="productName">Produto 1</div><title>Titulo do Produto 1</title>'
        link = 'http://www.epocacosmeticos.com.br/product/p'
        product = crawler.get_product(EpocaCosmeticos(), html_response, link)
        self.assertEquals('Produto 1', product.name)
        self.assertEquals('Titulo do Produto 1', product.title)
        self.assertEquals(link, product.url)