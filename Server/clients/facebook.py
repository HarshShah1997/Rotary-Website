"""
Author: harsh
"""
import requests
import json

HOST_URL = "https://graph.facebook.com"
FILE_NAME = 'config.json'


class FacebookClient(object):

    def __init__(self):
        config = retrieve_config()
        self.access_token = config['AccessToken']
        self.page_id = config['PageID']

    def get_photos(self):
        url = "{}/photos?type=uploaded&fields=album,picture,created_time".format(self.page_id)
        return get_data(url, self.access_token)


def generate_page_list(user_token):
    url = "{}/me/accounts?access_token={}".format(HOST_URL, user_token)
    return get_data_from_url(url)


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


def generate_and_store_token(user_token, app_id, app_secret, page_id):
    page_access_token = generate_long_page_access_token(user_token, app_id, app_secret, page_id)
    with open(FILE_NAME, 'w') as f:
        f.write(page_access_token)


def retrieve_config():
    with open(FILE_NAME, 'rb') as f:
        return json.loads(str(f.read(), 'utf-8'))


def generate_token_prompt():
    user_token = input("User token: ")
    app_id = input("App ID: ")
    app_secret = input("App Secret: ")
    page_id = input("Page ID: ")
    generate_and_store_token(user_token, app_id, app_secret, page_id)


def get_field(byte_str, field):
    print(byte_str)
    return json.loads(str(byte_str, 'utf-8'))[field]


def get_data(url, access_token):
    return get_data_from_url("{}/{}&access_token={}".format(HOST_URL, url, access_token))


def get_data_from_url(url):
    return get_field(requests.get(url).content, 'data')

