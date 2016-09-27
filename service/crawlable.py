# coding: utf-8

from abc import ABCMeta, abstractmethod

class Crawlable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_crawlable_name(self):
        pass

    @abstractmethod
    def get_category_pages(self):
        pass

    @abstractmethod
    def get_product_pages(self):
        pass

    @abstractmethod
    def get_home_page(self):
        pass

    @abstractmethod
    def get_product_name(self):
        pass

    def get_product_title(self):
        return '//title/text()'