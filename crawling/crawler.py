# coding: utf-8

from model.product import Product

class Crawler:
    
    def get_product(self, crawlable):
        return Product(
                    name = crawlable.get_product_name(),
                    title= crawlable.get_product_title(),
                    url  = crawlable.get_product_url(),
                )

    def crawl(self, crawlable_list):
        product_list = []
        for crawlable in crawlable_list:
            product_list.append(self.get_product(crawlable))
        return product_list