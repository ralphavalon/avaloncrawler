# coding: utf-8

import __builtin__, csv, io, codecs
from mox import Mox
from datetime import datetime
from unittest import TestCase

from model.product import Product
from service.impl.csv_exporter import CSVExporter


class CSVExporterTest(TestCase):
    def test_get_filename(self):
        exporter = CSVExporter()
        today = datetime.strftime(datetime.now(), '%Y-%m-%d')

        self.assertEquals('Product'+today+'.csv', exporter.__get_filename__('Product'))

    def test_get_row(self):
        exporter = CSVExporter()
        product = Product(name='pname', title='ptitle', url='purl')

        self.assertEquals(['pname', 'ptitle', 'purl'], exporter.__get_row__(product, product.get_exportable_attrs()))

    def test_export_with_success(self):
        exporter = CSVExporter()
        product = Product(name='pname', title='ptitle', url='purl')
        writer, stream = self.get_writer()
        mock = Mox()
        mock.StubOutWithMock(__builtin__, 'open')
        filename = exporter.__get_filename__('Product')
        open(filename, 'w').AndReturn(stream)
        mock.ReplayAll()
        
        exporter.export('Product', [product])
        
        mock.VerifyAll()
        mock.UnsetStubs()
    
    def test_export_with_empty_list(self):
        exporter = CSVExporter()

        with self.assertRaises(Exception):
            exporter.export('Product', [])
        

    def test_write(self):
        exporter = CSVExporter()
        product = Product(name='pname', title='ptitle', url='purl')
        writer, stream = self.get_writer()
        exportable_list = [product]
        exporter.__write__(writer, exportable_list)

        self.assertEquals('pname,ptitle,purl\r\n', stream.getvalue())

    def get_writer(self):
        stream = io.BytesIO()
        writer = csv.writer(codecs.getwriter('utf-8')(stream))
        return writer, stream