# coding: utf-8

from crawling.crawler import Crawler
from service.impl.epoca_cosmeticos import EpocaCosmeticos

crawler = Crawler()
crawled_dict = crawler.crawl([
                     EpocaCosmeticos()
                ])
print crawled_dict