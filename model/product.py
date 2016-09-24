# coding: utf-8

from service.exportable import Exportable

class Product(Exportable):

    def __init__(self, name, title, url):
        self.name = name
        self.title = title
        self.url = url

    def get_exportable_attrs(self):
        return ['name', 'title', 'url']