# coding: utf-8

from mox import Mox
import urlparse, os
from unittest import TestCase
from crawling.crawler import Crawler
from service.impl.epoca_cosmeticos import EpocaCosmeticos

class CrawlerTest(TestCase):
    
    def test_crawl(self):
        urlparse.urljoin = self.urljoin
        
        crawler = Crawler()
        epocaCosmeticos = EpocaCosmeticos()
        epocaCosmeticos.get_category_pages = self.get_category_pages
        epocaCosmeticos.get_product_pages = self.get_product_pages
        crawled_dict = crawler.crawl([
                            epocaCosmeticos
                        ])

        base_path = os.path.abspath('.') + os.sep + 'tests'
        file_base_path = 'file:///' + base_path
        products = crawled_dict['EpocaCosmeticos']
        self.assertEquals(1, len(crawled_dict))
        self.assertEquals(2, len(products))
        self.assertEquals('Produto 1', products[0].name)
        self.assertEquals('Titulo do Produto 1', products[0].title)
        self.assertTrue(os.path.join(base_path, 'produto_1.html') in products[0].url)
        self.assertEquals('Produto 2', products[1].name)
        self.assertEquals('Titulo do Produto 2', products[1].title)
        self.assertTrue(os.path.join(base_path, 'produto_2.html') in products[1].url)

    def urljoin(self, base, url):
        base = os.path.normpath(base + os.sep + os.pardir)
        return os.path.join(base, url)

    def get_category_pages(self):
        base_path = os.path.abspath('.') + os.sep + 'tests'
        file_base_path = 'file:///' + base_path
        return [os.path.join(file_base_path, 'home.html'), os.path.join(file_base_path, 'categoria_1.html')]
    
    def get_product_pages(self):
        return '.*produto.*.html$'