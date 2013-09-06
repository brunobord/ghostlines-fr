#!/usr/bin/env python
#-*- coding: utf-8 -*-
import codecs

from jinja2 import Template
from markdown import Markdown


class MarkdownReader(object):
    "Reader for markdown documents"
    file_extensions = ['md', 'markdown', 'mkd']
    extensions = ['extra', 'meta', 'tables', 'toc', 'admonition']

    def read(self, source_path):
        """Parse content and metadata of markdown files"""
        text = codecs.open(source_path, encoding='utf').read()
        md = Markdown(extensions=self.extensions)
        content = md.convert(text)
        return content


class HTMLWriter(object):
    "HTML Writer, builds documentation"
    def __init__(self, template):
        self.template = template

    def write(self, data):
        "Write content to the destination path"
        destination = 'index.html'
        with codecs.open(destination, 'w', encoding='utf') as fd:
            fd.write(self.template.render(data))


if __name__ == '__main__':
    reader = MarkdownReader()
    writer = HTMLWriter(Template(codecs.open('templates/base.html', encoding='utf').read()))
    content = reader.read('ghost-lines-fr.md')
    writer.write({'content': content})

