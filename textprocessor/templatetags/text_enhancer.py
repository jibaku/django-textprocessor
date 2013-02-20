# -*- coding: utf-8 -*-
import re

import markdown
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django import template


register = template.Library()


@register.filter
@stringfilter
def twitter_username(value):
    """Add a link to twitter for the twitter user reference in a string

    >>> twitter_username("Hello, @ev")
    u'Hello, <a href="http://twitter.com/ev">@ev</a>'
    """
    def repl(m):
        return '<a href="http://twitter.com/%(username)s">@%(username)s</a>' % {'username': m.group(1)}
    return re.sub(r"@(\w+)", repl, value)


@register.filter(name='markdown')
@stringfilter
def markdown_filter(value):
    html = markdown.markdown(value, output_format="html5")
    return mark_safe(html)
