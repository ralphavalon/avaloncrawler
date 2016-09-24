# coding: utf-8

from model.product import Product

class Crawler:
    
    def crawl(self, crawlable_list):
        product_list = []
        for crawlable in crawlable_list:
            product_list.append(
                Product(
                    name = crawlable.get_product_name(),
                    title= crawlable.get_product_title(),
                    url  = crawlable.get_product_url(),
                )
            )
        return product_list