from django import template
import re
import pygments
from pygments.lexers import LEXERS, get_lexer_by_name
from pygments import highlight
from pygments.formatters import HtmlFormatter

register = template.Library()

regex = re.compile(r'<code>(.*?)</code>', re.DOTALL)

@register.filter(name='codesyntax')
def codesyntax(code, lang=None):

    guess = 'python3'
    if code.lstrip().startswith('<?php'):
        guess = 'php'
    elif code.lstrip().startswith('<'):
        guess = 'html'
    elif code.lstrip().startswith(('function', 'var', '$')):
        guess = 'javascript'
    lexer = get_lexer_by_name(lang or guess, stripall=True)
    return highlight(code, lexer, HtmlFormatter())

