=====
Usage
=====

Describes how to use textprocessor when it is installed and configured.

Templatetags
============

textprocessor provides various template tags that can be used to enhance the
content displayed to the user.

twitter_username
----------------

The ``twitter_username`` looks for @username in the value passed to the filter
and add the link to the given username on the Twitter.com website::

    {{ content|twitter_username }}


markdown_filter
---------------

The ``markdown`` filter convert the value passed to the filter and convert
it to markdown using the `markdown <https://pypi.python.org/pypi/Markdown>`_
library::

    {{ content|markdown }}
