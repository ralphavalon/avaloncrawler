﻿# coding: utf-8

import csv
from ..exporter import Exporter
from datetime import datetime
import sys, traceback

class CSVExporter(Exporter):

    def __get_row__(self, exportable, exportable_attrs):
        row = []
        for attr in exportable_attrs:
            row.append(getattr(exportable, attr))
        return row
        
    def __write__(self, outputWriter, exportable_list):
        print('Writing products to the csv...')
        for exportable in exportable_list:
            exportable_attrs = exportable.get_exportable_attrs()
            try:
                outputWriter.writerow(self.__get_row__(exportable, exportable_attrs))
            except Exception as e:
                traceback.print_exc(file=sys.stdout)

            
    def __get_filename__(self, filename_prefix):
        today = datetime.strftime(datetime.now(), '%Y-%m-%d')
        return '%s%s.csv' % (filename_prefix, today)

    def export(self, filename_prefix, exportable_list):
        if(exportable_list):
            filename = self.__get_filename__(filename_prefix)
            outputFile = open(filename, 'w')
            print('Creating %s' %(filename))
            outputWriter = csv.writer(outputFile)
            self.__write__(outputWriter, exportable_list)
            outputFile.close()
            print('Done.')
        else:
            raise Exception('No results')
