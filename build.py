#!/usr/bin/env python
#-*- coding: utf-8 -*-
from os.path import abspath, dirname, join, splitext
from os import listdir
import codecs

from jinja2 import Template
from markdown import Markdown

ROOT_DIR = abspath(dirname(__file__))
SOURCE_DIR = join(ROOT_DIR, 'src')

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
    data = {}
    for filename in listdir(SOURCE_DIR):
        key, _ = splitext(filename)
        key = key.replace('-', '_')
        content = reader.read(join(SOURCE_DIR, filename))
        data[key] = content
    writer.write(data)

