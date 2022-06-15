from flask import Flask, request, escape, send_file
import os
import requests
from PIL import Image

settings = {
'land':'arcgis/rest/services/PKK6/CadastreObjects/MapServer/export?layers=show%3A21&format=PNG32',
'building':'arcgis/rest/services/PKK6/CadastreObjects/MapServer/export?layers=show%3A30&format=PNG32',
'boundary':'arcgis/rest/services/PKK6/BordersGKN/MapServer/export?layers=show%3A0%2C5%2C16%2C25%2C32&format=PNG32',
'zone':'arcgis/rest/services/PKK6/Zones/MapServer/export?layers=show%3A0%2C5%2C6%2C11&format=PNG32'
}

pkk = Flask(__name__, static_url_path='')

#Тест
@pkk.route('/')
def index():
    return 'It works!'

@pkk.route('/path/<path:subpath>')
def static_file(subpath):
    bbox = str(request.args.get('bbox'))
    os.makedirs('cache/'+escape(subpath)+'/', exist_ok=True)
    if not os.path.isfile('cache/'+escape(subpath)+'/'+bbox+'.png'):
        r = requests.get('https://pkk.rosreestr.ru/'+settings[escape(subpath)]+'&bbox='+bbox+'&bboxSR=102100&imageSR=102100&size=1024%2C1024&transparent=true&f=image', verify=False)  
        with open('cache/'+escape(subpath)+'/'+bbox+'.png', 'wb') as f:
            f.write(r.content)
    return send_file('cache/'+escape(subpath)+'/'+bbox+'.png', mimetype='image/png')
