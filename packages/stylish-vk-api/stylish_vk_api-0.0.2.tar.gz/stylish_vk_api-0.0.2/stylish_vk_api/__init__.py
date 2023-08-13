import os
import re
import time
import vk_api
import random
import requests
from dotenv import load_dotenv

def load_access_token():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)



def parse_vk_link(link):
    item_id = None
    owner_id = None
    
    match_wall = re.match(r'https://vk\.com/wall(-?\d+)_(\d+)', link)
    match_id = re.match(r'https://vk\.com/id(\d+)\?w=wall(\d+)_(\d+)', link)
    
    if match_wall:
        owner_id = int(match_wall.group(1))
        item_id = int(match_wall.group(2))
    elif match_id:
        owner_id = int(match_id.group(1))
        item_id = int(match_id.group(3))
    
    return owner_id, item_id



def is_valid_vk_link(link):
    return bool(parse_vk_link(link))



def like(url_for_like):
    load_access_token()
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    
    owner_id, item_id = parse_vk_link(url_for_like)
    
    if owner_id is None or item_id is None:
        print("Некорректная ссылка")
        return

    print("owner_id:", owner_id)
    print("item_id:", item_id)

    url = "https://api.vk.com/method/likes.add"

    params = {
        "access_token": ACCESS_TOKEN,
        "item_id": item_id,
        "owner_id": owner_id,
        "type": "post",
        "v": "5.157"
    }

    headers = {
        "User-Agent": "KateMobileAndroid/103-540 (Android 9; SDK 28; x86; Google AOSP on IA Emulator; en)",
        "Accept-Encoding": "gzip, deflate"
    }

    response = requests.get(url, params=params, headers=headers)

    print(response.text)

# like('https://vk.com/wall-188806182_17698')
# like('https://vk.com/id774207693?w=wall774207693_1')


def online(execution_time):
    load_access_token()
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

    url = 'https://api.vk.com/method/account.setOnline'

    params = {
        'access_token': ACCESS_TOKEN, # https://vkhost.github.io
        'v': '5.131'
    }

    headers = {
        'User-Agent': 'KateMobileAndroid/103-540 (Android 9; SDK 28; x86; Google AOSP on IA Emulator; en)',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'Keep-Alive'
    }

    start_time = time.time()

    while time.time() - start_time < execution_time:
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            print('Запрос успешно выполнен!')
            data = response.json()
            print(data)
        else:
            print('Произошла ошибка при выполнении запроса. Код ошибки:', response.status_code)
            exit()

        time.sleep(25)


# online(60)


def get_user_id(user_link):
    id = user_link
    if 'vk.com/' in user_link: 
        id = user_link.split('/')[-1]
    if not id.replace('id', '').isdigit():
        id = vkapi.utils.resolveScreenName(screen_name=id)['object_id']
    else:
        id = id.replace('id', '')
    return int(id)

# print(get_user_id('https://vk.com/id774207693'))


def send_message(user_link, message_text):
    load_access_token()
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    
    vk_id = get_user_id(user_link)

    url = 'https://api.vk.com/method/messages.send'
    random_id = random.randint(10**12, (10**13)-1)

    params = {
        'access_token': ACCESS_TOKEN, # https://vkhost.github.io
        'message': message_text,
        'peer_id': vk_id,
        'random_id': random_id,
        'v': '5.131'
    }

    headers = {
        'User-Agent': 'KateMobileAndroid/103-540 (Android 9; SDK 28; x86; Google AOSP on IA Emulator; en)',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'Keep-Alive',
        'Content-Length': '304'
    }

    response = requests.post(url, data=params, headers=headers)
    if __name__ == '__main__':
        if response.status_code == 200:
            print('Запрос успешно выполнен!')
            data = response.json()
            print(data)
        else:
            print('Произошла ошибка при выполнении запроса. Код ошибки:', response.status_code)


# send_message('https://vk.com/id774207693', 'teeeest')


def change_status(text):
    load_access_token()
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    
    url = "https://api.vk.com/method/status.set"

    params = {
        "access_token": ACCESS_TOKEN,
        "text": text,
        "v": "5.131"
    }

    headers = {
        "User-Agent": "KateMobileAndroid/103-540 (Android 9; SDK 28; x86; Google AOSP on IA Emulator; en)",
        "Accept-Encoding": "gzip, deflate"
    }

    response = requests.get(url, params=params, headers=headers)
    print(response.text)

# change_status('test')


def comment(url_for_comment, text):
    load_access_token()
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

    owner_id, item_id = parse_vk_link(url_for_comment)
    
    if owner_id is None or item_id is None:
        print("Некорректная ссылка")
        return

    print("owner_id:", owner_id)
    print("item_id:", item_id)

    url = "https://api.vk.com/method/wall.createComment"

    headers = {
        "User-Agent": "KateMobileAndroid/103-540 (Android 9; SDK 28; x86; Google AOSP on IA Emulator; en)",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "access_token": ACCESS_TOKEN, 
        "message": text,
        "owner_id": owner_id,
        "post_id": item_id,
        "v": "5.131"
    }

    response = requests.post(url, headers=headers, data=data)
    print(response.text)

# comment('https://vk.com/wall774207693_36', 'teeesstt')
# comment('https://vk.com/wall-193984556_107464', 'teeest')


def wall_post(url_for_post, text):
    load_access_token()
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    
    owner_id = get_user_id(url_for_post)

    url = "https://api.vk.com/method/wall.post"

    payload = {
        "access_token": ACCESS_TOKEN, # https://vkhost.github.io
        "message": text,
        "owner_id": owner_id,
        "services": "twitter,facebook",
        "v": "5.131"
    }

    headers = {
        "User-Agent": "KateMobileAndroid/103-540 (Android 9; SDK 28; x86; Google AOSP on IA Emulator; en)",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate"
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.text)

# wall_post('https://vk.com/id774207693', 'test post..')
# wall_post('https://vk.com/public222010715', 'test wall post in test public')
