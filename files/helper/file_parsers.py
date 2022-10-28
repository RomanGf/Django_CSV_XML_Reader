import csv
import datetime
import xml.etree.ElementTree as ET

from .regexp import edit_word


def csv_parser(path):
    list_csv_users = []

    with open(path, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0 or row[0] == '' or row[1] == '' or row[2] == '':
                pass
            else:
                username = edit_word(row[0])
                password = row[1]
                date_joined = datetime.date.fromtimestamp(int(row[2]))
                list_csv_users.append({
                    'username': username,
                    'password': password,
                    'date_joined': date_joined
                })
    return list_csv_users


def xml_parser(path):
    list_xml_users = []
    tree = ET.parse(path)
    root = tree.getroot()
    all_users = root.find('user')
    users = all_users.find('users')
    for c in users.findall('user'):
        first_name = c.find('first_name').text
        last_name = c.find('last_name').text
        avatar = c.find('avatar').text
        if first_name == None or last_name == None:
            continue
        if '(' in first_name or '(' in last_name:
            first_name = edit_word(first_name)
        if first_name == '' or last_name == '':
            continue
        list_xml_users.append({
            'username': f'{first_name[0]}.{last_name}',
            'avatar': avatar
        })
    return list_xml_users