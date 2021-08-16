import requests
from os import path

from icon_path import IconPath


assets_path = './assets/'
lihkg_url_prefix = 'https://cdn.lihkg.com/assets/faces/'


if __name__ == '__main__':
    for icon_path in IconPath.all:
        file_path = assets_path + icon_path.replace('/', '_') + '.gif'

        if not path.exists(file_path):
            with open(file_path, 'wb') as f:
                target = lihkg_url_prefix + icon_path + '.gif'
                f.write(requests.get(target).content)
                print('Downloading', icon_path, '......')
