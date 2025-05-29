from flask import Flask, request, send_file
from markupsafe import escape
import os
from random import random
import requests
import urllib3

settings = {
    'land': 36048,
    'building': 36049,
}
headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'ru-RU,ru;q=0.9',
    'origin': 'https://nspd.gov.ru',
    'priority': 'i',
    'referer': 'https://nspd.gov.ru/map?thematic=PKK&zoom=10.6826410043574285&coordinate_x=5241461.661219545&coordinate_y=7231818.562737224&theme_id=1&is_copy_url=true&active_layers=36048',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
pkk = Flask(__name__, static_url_path='')


# Тест
@pkk.route('/')
def index():
    return 'It works!'


@pkk.route('/path/<path:subpath>')
def static_file(subpath):
    bbox = str(request.args.get('bbox'))
    os.makedirs('cache2/'+escape(subpath)+'/', exist_ok=True)
    if not os.path.isfile('cache2/'+escape(subpath)+'/'+bbox+'.png'):
        layer_id = settings[escape(subpath)]
        r = requests.get('https://nspd.gov.ru/api/aeggis/v3/' + str(layer_id) + '/wms', params={
            'REQUEST': 'GetMap',
            'SERVICE': 'WMS',
            'VERSION': '1.3.0',
            'FORMAT': 'image/png',
            'STYLES': '',
            'TRANSPARENT': 'true',
            'LAYERS': layer_id,
            'RANDOM': random(),
            'WIDTH': '512',
            'HEIGHT': '512',
            'CRS': 'EPSG:3857',
            'BBOX': bbox
        }, headers=headers, verify=False)
        with open('cache2/'+escape(subpath)+'/'+bbox+'.png', 'wb') as f:
            f.write(r.content)
    return send_file('cache2/'+escape(subpath)+'/'+bbox+'.png', mimetype='image/png')
