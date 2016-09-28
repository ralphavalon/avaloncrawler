# coding: utf-8

from service.exportable import Exportable
from util.utils import get_normalized_data
import unicodedata

class Product(Exportable):

    def __init__(self, name, title, url):
        self.name = get_normalized_data(name)
        self.title = get_normalized_data(title)
        self.url = url

    def get_exportable_attrs(self):
        return ['name', 'title', 'url']