# -*- coding: utf-8 -*-
import requests


def load_file(url, file_path='./p.png'):
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)


if __name__ == '__main__':
    load_file(url="https://habrastorage.org/getpro/moikrug/uploads/company/241/654/114/logo/medium_76b35e40e40f45260eb8452e5de446c3.png")
