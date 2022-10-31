import datetime

from django.test import TestCase

from ..helper.file_parsers import parse_csv_row, map_to_model, get_user_from_xml_element


class TestParser(TestCase):

    def test_parse_cvs_row_should_return_object_when_correct_row_passed(self):
        actual = parse_csv_row(['Roman', 'dalsdazxc123dD', '1421161336'])
        expected = {
            'username': 'Roman',
            'password': 'dalsdazxc123dD',
            'date_joined': datetime.date.fromtimestamp(int('1421161336'))
        }

        self.assertEquals(actual, expected)

    def test_parse_cvs_row_should_return_edited_when_parentheses_passed(self):
        actual = parse_csv_row(['R(om)an', 'dalsdazxc123dD', '1421161336'])
        expected = {
            'username': 'Ran',
            'password': 'dalsdazxc123dD',
            'date_joined': datetime.date.fromtimestamp(int('1421161336'))
        }

        self.assertEquals(actual, expected)

    def test_map_to_models_should_return_correct_model_when_user_object_passed(self):
        actual = map_to_model({
            'first_name': 'Roman',
            'last_name': 'Hafiak',
            'avatar': 'https://pbs.twimg.com/media/BcINeMVCIAABeWd.jpg'
        })

        expected = {
            'username': 'R.Hafiak',
            'avatar': 'https://pbs.twimg.com/media/BcINeMVCIAABeWd.jpg'
        }
        self.assertEquals(actual, expected)
