# coding: utf-8

from service.exportable import Exportable
import unicodedata

class Product(Exportable):

    def __init__(self, name, title, url):
        self.name = self.__remove_accents__(self.__get_unicode__(name))
        self.title = self.__remove_accents__(self.__get_unicode__(title))
        self.url = url

    def get_exportable_attrs(self):
        return ['name', 'title', 'url']

    def __remove_accents__(self, unicode_input):
        nfkd_form = unicodedata.normalize('NFKD', unicode_input)
        return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

    def __get_unicode__(self, input):
        if type(input) == unicode:
            return input
        else:
            try:
                return unicode(input) 
            except UnicodeDecodeError:
                return unicode(input, 'latin1')