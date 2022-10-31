import csv
import datetime
import xml.etree.ElementTree as ET

from .regexp import edit_word


def parse_csv_row(row):
    username = edit_word(row[0])
    password = row[1]
    date_joined = datetime.date.fromtimestamp(int(row[2]))
    return {
        'username': username,
        'password': password,
        'date_joined': date_joined
    }


def parse_csv_file(path):
    list_csv_users = []

    with open(path, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0 or any(x == '' for x in row):
                pass
            else:
                list_csv_users.append(parse_csv_row(row))
    return list_csv_users


def map_to_model(user):
    if not user['first_name'] or not user['last_name']:
        return
    
    if '(' in user['first_name'] or ')' in user['last_name']:
        user['first_name'] = edit_word(user['first_name'])
    
    if not user['first_name']:
        return

    return {
        'username': f'{user["first_name"][0]}.{user["last_name"]}',
        'avatar': user["avatar"]
    }


def parse_xml_file(path):
    tree = ET.parse(path)
    root = tree.getroot()
    all_users = root.find('user').find('users').findall('user')
    list_xml_users = map(
        map_to_model,
        map(
            get_user_from_xml_element,
            all_users))
    
    return list(filter(
        lambda x: x is not None,
        list_xml_users))


def get_user_from_xml_element(element):
    return {
        'first_name': element.find('first_name').text,
        'last_name': element.find('last_name').text,
        'avatar': element.find('avatar').text
    }