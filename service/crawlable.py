# coding: utf-8

from abc import ABCMeta, abstractmethod

class Crawlable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_category_page(self):
        pass

    @abstractmethod
    def get_product_page(self):
        pass

    @abstractmethod
    def get_product_name(self):
        pass

    @abstractmethod
    def get_product_title(self):
        pass

    @abstractmethod
    def get_product_url(self):
        pass