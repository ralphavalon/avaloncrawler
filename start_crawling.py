# coding: utf-8

from crawling.crawler import Crawler
from service.impl.epoca_cosmeticos import EpocaCosmeticos
from service.impl.csv_exporter import CSVExporter

crawler = Crawler()
crawled_dict = crawler.crawl([
                     EpocaCosmeticos()
                ], max_delay=5)

exporter = CSVExporter()

for crawlable_name, exportable_list in crawled_dict.iteritems():
    exporter.export(crawlable_name, exportable_list)