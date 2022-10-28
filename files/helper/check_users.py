def check_users(list_csv_users, list_xml_users):
    list_user = []
    for i in range(len(list_csv_users)):
        for j in range(len(list_xml_users)):
            if list_csv_users[i]['username'] == list_xml_users[j]['username']:
                list_user.append({
                    "username": list_csv_users[i]['username'],
                    "password": list_csv_users[i]['password'],
                    "date_joined": list_csv_users[i]['date_joined'],
                    "avatar": list_xml_users[j]['avatar']
                })
    return list_user