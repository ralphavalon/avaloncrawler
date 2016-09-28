# coding: utf-8

import unicodedata
from lxml.etree import _ElementUnicodeResult

def get_normalized_data(input):
    return __remove_accents__(__get_unicode__(input))

def __remove_accents__(unicode_input):
    nfkd_form = unicodedata.normalize('NFKD', unicode_input)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def __get_unicode__(input):
    if type(input) == unicode:
        return input
    elif type(input) == _ElementUnicodeResult:
        return unicode(input)
    else:
        try:
            return unicode(input).encode('latin1').decode('utf8')
        except UnicodeDecodeError:
            print type(input)
            return unicode(input, 'latin1').encode('latin1').decode('utf8')
