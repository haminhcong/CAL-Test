import requests

ROOT_URL = "http://127.0.0.1:8004/"


def login_site(session, user_name, password):
    try:
        login_url = ROOT_URL + "auth/api_login/"
        session.get(login_url)
        csrftoken = session.cookies['csrftoken']
        login_resp = session.post(login_url,
                                  data={'csrfmiddlewaretoken': csrftoken,
                                        'user_name_email': user_name,
                                        'password': password})
        # check if login is success or not

        if login_resp.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        return False


# session = requests.Session()
#
# # access url without authenticate
# try:
#     without_auth_url = "admin/system/cluster_list"
#     r = session.get(ROOT_URL + without_auth_url, timeout=105)
#     status_code = r.status_code
#     pass
# except Exception as e:
#     pass
# session.close()

# access url secured by permission admin
session = requests.Session()
is_login = login_site(session, 'admin', 'bkcloud')
if is_login:
    try:
        secured_url = "admin/system/cluster_list"
        r = session.get(ROOT_URL + secured_url, timeout=105)
        resp_data  = r.json()
        status_code = r.status_code
        if status_code ==200:
            pass
        else:
            pass
    except Exception as e:
        pass
session.close()
#
# # access url secured by permission admin by normal user
# session = requests.Session()
# is_login = login_site(session, 'haminhcong', 'bkhmc20130447')
# if is_login:
#     try:
#         secured_url = "admin/system/cluster_list"
#         r = session.get(ROOT_URL + secured_url, timeout=105)
#         status_code = r.status_code
#         pass
#     except Exception as e:
#         pass
# session.close()
#
# # access url secured by permission admin by normal user
# session = requests.Session()
# try:
#     secured_url = "admin/system/cluster_list"
#     r = session.get(ROOT_URL + secured_url, timeout=105)
#     status_code = r.status_code
#     pass
# except Exception as e:
#     pass
# session.close()
