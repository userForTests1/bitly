import os
import requests
import logging
import argparse
from dotenv import load_dotenv
import urllib.parse as urlparse


load_dotenv()
BITLY_APIKEY = os.environ['BITLY_APIKEY']
HEADERS = {
    'Authorization': BITLY_APIKEY,
    'Content-Type': 'application/json',
}


def create_parser():
    parser = argparse.ArgumentParser(
        description='Скрипт для сокращения ссылок через сервис https://bit.ly '
                    'и получение количества кликов на сокращенной ссылке'
    )
    parser.add_argument('url', help='Ссылка для работы')
    return parser


def is_bitlink(url, apikey):
    headers = {
        'Authorization': f'Bearer {apikey}',
        'Content-Type': 'application/json',
    }
    parsed = urlparse.urlparse(url)
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/'
                            f'{parsed.netloc}/{parsed.path}',
                            headers=headers)
    return response.ok


def shorten_link(url, apikey):
    headers = {
        'Authorization': f'Bearer {apikey}',
        'Content-Type': 'application/json',
    }
    params = {
        "long_url": url,
    }
    response = requests.post('https://api-ssl.bitly.com/v4/shorten',
                             headers=headers, json=params)
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(url, apikey):
    headers = {
        'Authorization': f'Bearer {apikey}',
        'Content-Type': 'application/json',
    }
    params = {
        'unit': 'month',
        'units': -1
    }
    parsed = urlparse.urlparse(url)
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/'
                             f'{parsed.netloc}/{parsed.path}/clicks/summary',
                             headers=headers, params=params)
    response.raise_for_status()
    return response.json()["total_clicks"]


def main():
    parser = create_parser()
    args = parser.parse_args()
    url = args.url
    need_short = is_bitlink(url, BITLY_APIKEY)
    try:
        if need_short:
            clicks = count_clicks(url, BITLY_APIKEY)
            print(f'По Вашей ссылке перешли: {clicks} раз(а)')
        else:
            link = shorten_link(url, BITLY_APIKEY)
            print(f'Битлинк: {link}')
    except requests.exceptions.HTTPError as err:
        logging.error(err)


if __name__ == '__main__':
    main()
