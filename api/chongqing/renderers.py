#-*- coding: UTF-8 -*-
from django.utils import six
from django.utils.six import StringIO
from django.utils.xmlutils import SimplerXMLGenerator
from django.utils.encoding import smart_text
from rest_framework.renderers import BaseRenderer

class XMLRenderer(BaseRenderer):
    media_type = 'application/xml'
    format = 'xml'
    charset = 'utf-8'
    item_tag_name = 'list-item'
    root_tag_name = 'responseDatas'
    idx = 0

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if data is None:
            return ''
        return data

    def get_xml(self, data, item_name):
        if data is None:
            return ''
        stream = StringIO()
        xml = SimplerXMLGenerator(stream, self.charset)
        xml.startDocument()
        xml.startElement(self.root_tag_name, {})
        self._to_xml(xml, data, item_name, 0)
        xml.endElement(self.root_tag_name)
        xml.endDocument()
        return stream.getvalue()

    def _to_xml(self, xml, data, item_name, depth):
        if isinstance(data, (list, tuple)):
            for item in data:
                if depth != 0:
                    xml.startElement(item_name[depth][self.idx], {})
                    self._to_xml(xml, item, item_name, depth + 1)
                    xml.endElement(item_name[depth][self.idx])
                else:
                    xml.startElement(item_name[depth][0], {})
                    self._to_xml(xml, item, item_name, depth + 1)
                    xml.endElement(item_name[depth][0])
            if depth == 1:
                self.idx = self.idx + 1
                if self.idx >= len(item_name[depth]):
                    self.idx = 0
        elif isinstance(data, dict):
            for key, value in six.iteritems(data):
                xml.startElement(key, {})
                self._to_xml(xml, value, item_name, depth)
                xml.endElement(key)
        elif data is None:
            pass
        else:
            xml.characters(smart_text(data))