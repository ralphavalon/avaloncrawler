# coding: utf-8

from abc import ABCMeta, abstractmethod

class Exportable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_exportable_attrs(self):
        pass