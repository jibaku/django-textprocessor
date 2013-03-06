from unittest import TestCase

from textprocessor.templatetags.text_enhancer import twitter_username


class SimpleTest(TestCase):

    def test_twitter_username(self):
        value = "Hello, @ev"
        expected = u'Hello, <a href="http://twitter.com/ev">@ev</a>'
        self.assertEqual(twitter_username(value), expected)

        value = "Hello, @ev how are you ?"
        expected = u'Hello, <a href="http://twitter.com/ev">@ev</a> how are you ?'
        self.assertEqual(twitter_username(value), expected)

        value = "Hello, @ev, @twitter and @bob how are you ?"
        expected = u'Hello, <a href="http://twitter.com/ev">@ev</a>, <a href="http://twitter.com/twitter">@twitter</a> and <a href="http://twitter.com/bob">@bob</a> how are you ?'
        self.assertEqual(twitter_username(value), expected)
