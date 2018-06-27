"""
Author: harsh
"""
import requests
import json

HOST_URL = "https://graph.facebook.com"
FILE_NAME = 'clients/token.txt'


class FacebookClient(object):

    def __init__(self, page_id):
        self.access_token = retrieve_access_token()
        self.page_id = page_id

    def get_photos(self):
        pass




def generate_page_list(user_token):
    url = "{}/me/accounts?access_token={}".format(HOST_URL, user_token)
    return get_field(requests.get(url).content, 'data')


def generate_long_user_token(short_user_token, app_id, app_secret):
    url = "{}/oauth/access_token?" \
          "grant_type=fb_exchange_token&" \
          "client_id={}&" \
          "client_secret={}&" \
          "fb_exchange_token={}".format(HOST_URL, app_id, app_secret, short_user_token)
    
    response = requests.get(url)
    return get_field(response.content, 'access_token')


def generate_long_page_access_token(short_user_token, app_id, app_secret, page_id):
    long_user_access_token = generate_long_user_token(short_user_token, app_id, app_secret)
    long_page_access_token = parse_page_access_token(
        generate_page_list(long_user_access_token),
        page_id
    )
    return long_page_access_token


def parse_page_access_token(page_list, page_id):
    for page in page_list:
        if page['id'] == page_id:
            return page['access_token']
    print("No such page found")


def get_field(byte_str, field):
    return json.loads(str(byte_str, 'utf-8'))[field]


def generate_and_store_token(user_token, app_id, app_secret, page_id):
    page_access_token = generate_long_page_access_token(user_token, app_id, app_secret, page_id)
    with open(FILE_NAME, 'w') as f:
        f.write(page_access_token)


def retrieve_access_token():
    with open(FILE_NAME) as f:
        return f.readline()


def generate_token_prompt():
    user_token = input("User token: ")
    app_id = input("App ID: ")
    app_secret = input("App Secret: ")
    page_id = input("Page ID: ")
    generate_and_store_token(user_token, app_id, app_secret, page_id)
