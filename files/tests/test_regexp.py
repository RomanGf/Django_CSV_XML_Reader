from django.test import TestCase

from ..helper.regexp import edit_word


class TextRegExp(TestCase):

    def test_edit_word_should_return_word_without_parentheses(self):
        word = edit_word('Hello(word)')

        self.assertEquals(word, 'Hello')

    def test_edit_word_should_return_whole_word_when_no_parentheses(self):
        word = edit_word('Hello')

        self.assertEquals(word, 'Hello')