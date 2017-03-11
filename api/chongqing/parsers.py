#-*- coding: UTF-8 -*-
from collections import OrderedDict
from rest_framework.parsers import BaseParser
import defusedxml.ElementTree as etree
#import decimal
#from django.conf import settings
#from django.utils import six
#from rest_framework.exceptions import ParseError

class XMLParser(BaseParser):
    media_type = 'application/xml'

    def parse(self, stream, media_type=None, parser_context=None):
        if stream is None:
            return ''
        return stream

    def get_seri(self, stream, item_name):
        assert etree, 'XMLParser requires defusedxml to be installed'
        #parser_context = {}
        #encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)
        #parser = etree.DefusedXMLParser(encoding=encoding)
        try:
            root = etree.fromstring(stream, forbid_dtd=True)
        except Exception, e:
            print e
            #raise ParseError('XML parse error - %s' % six.text_type(exc))
        data = self._xml_convert(root, item_name)
        return [OrderedDict(sorted(data[item_name[0][0]].items(),key=lambda t: len(t[0])))]

    def _xml_convert(self, element, item_name):
        children = list(element)
        if len(children) == 0:
            return self._type_convert(element.text)
        else:
            if len(item_name) < 2:
                data = {}
                for child in children:
                    data[child.tag] = self._xml_convert(child, item_name)
            else:
                found = False
                for item in item_name[1]:
                    if item == children[0].tag:
                        data = []
                        for child in children:
                            data.append(self._xml_convert(child, item_name))
                        found = True
                        break
                if found == False:
                    data = {}
                    for child in children:
                        data[child.tag] = self._xml_convert(child, item_name)            
            return data

    def _type_convert(self, value): # convert to PYTHON type
        if value is None:
            return value
#         try:
#             print value
#             return datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
#         except ValueError:
#             pass
#         try:
#             return int(value)
#         except ValueError:
#             pass
#         try:
#             return decimal.Decimal(value)
#         except decimal.InvalidOperation:
#             pass
        return value