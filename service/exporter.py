# coding: utf-8

from abc import ABCMeta, abstractmethod

class Exporter:
    __metaclass__ = ABCMeta

    @abstractmethod
    def export(self, filename_prefix, exportable_list):
        pass