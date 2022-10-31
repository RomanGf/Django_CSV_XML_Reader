import datetime
from django.test import TestCase

from ..helper.check_users import check_users


class TestCheckUser(TestCase):

    def test_check_users_should_return_concatenated_user_when_lists_have_same_user(self):
        list_csv_users = [{
            'username': 'R.Hafiak',
            'password': 'dalsdazxc123dD',
            'date_joined': datetime.date.fromtimestamp(int('1421161336'))
        }]
        list_xml_user = [{
            'username': 'R.Hafiak',
            'avatar': 'https://pbs.twimg.com/media/BcINeMVCIAABeWd.jpg'
        }]

        self.assertEquals(check_users(list_csv_users, list_xml_user),
                          [{
                              'username': 'R.Hafiak',
                              'password': 'dalsdazxc123dD',
                              'date_joined': datetime.date.fromtimestamp(int('1421161336')),
                              'avatar': 'https://pbs.twimg.com/media/BcINeMVCIAABeWd.jpg'
                          }])

    def test_check_users_should_return_empty_list_when_lists_dont_have_same_user(self):
        list_csv_users = [{
            'username': 'R.Hafiak',
            'password': 'dalsdazxc123dD',
            'date_joined': datetime.date.fromtimestamp(int('1421161336'))
        }]
        list_xml_user = [{
            'username': 'F.Mask',
            'avatar': 'https://pbs.twimg.com/media/BcINeMVCIAABeWd.jpg'
        }]

        actual = check_users(list_csv_users, list_xml_user)
        expected = []

        self.assertEquals(actual, expected)
