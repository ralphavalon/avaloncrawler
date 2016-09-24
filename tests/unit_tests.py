# coding: utf-8

from unittest import TestCase
from crawling.crawler import Crawler
from service.impl.epoca_cosmeticos import EpocaCosmeticos

class CrawlingTest(TestCase):
    def test_crawling(self):
        crawler = Crawler()
        crawled_list = crawler.crawl([
                            EpocaCosmeticos()
                        ])
        product = crawled_list[0]
        self.assertEquals(1, len(crawled_list))
        self.assertEquals('name', product.name)
        self.assertEquals('title', product.title)
        self.assertEquals('url', product.url)