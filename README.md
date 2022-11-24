# pkk-cache
## Описание
Данный скрипт делает запрос к сайту https://pkk.rosreestr.ru, созраняет скачанный файл на диск и выдаёт для отображения.
Создавался для JOSM, однако может использоваться и для других програм.

Если возникнут сложности, пишите мне в Telegram, буду рад помочь https://t.me/grass_snake

## Установка
1. Установите последнюю версию Python
  https://www.python.org/downloads/
Если Вы устанавливаете на Windows, то сразу при запуске установщика появится окно, внизу нужно выбрать галочку «Add Python 3.* to PATH».
![Python installator](https://docs.python.org/3/_images/win_installer.png)

2. Добавьте 3 библиотеки (введите в консоли):
```
pip3 install requests
pip3 install flask
pip3 install Pillow
```
Если не получилось, введите «pip» вместо «pip3».

Если появляется ошибка: «"pip3" не является внутренней или внешней командой,исполняемой программой или пакетным файлом», значит вернитесь в пункт 1 и обязательно проставьте галочку PATH, скорее всего проблема в этом.

3. Скачайте файл pkk-cache.py
  https://github.com/Grass-snake-89/pkk-cache

Если Вы работаете в Windows, то можете также скачать файл запуск кадастра.bat (при работе в других ОС он не нужен).

## Запуск скрипта

4. Запустите терминал в директории с файлом.
    - При работе в **Linux** выполните команду:
    ```
    export FLASK_APP=pkk-cache && flask run
    ```
    Примечание: если не получилось, попробуйте выполнить две отдельные команды:
    ```
    export FLASK_APP=pkk-cache
    flask run
    ```

    - При работе в **Windows** можно запустить файл «запуск кадастра.bat», который расположен в той-же директории, что и «pkk-cache.py». Он запустит скрипт автоматически.
    
    Если запуск bat-файла не подходит, то можно  выполните команду в консоли (запуск в той папке, где разположен «pkk-cache.py»):

    ```
    set FLASK_APP=pkk-cache && flask run
    ```
    Примечание: если не получилось, попробуйте выполнить две отдельные команды:

    ```
    set FLASK_APP=pkk-cache
    flask run
    ```

    - Другие способы запуска (**Fish**, **Powershell**) указаны на странице [Документацию Flask](https://flask.palletsprojects.com/en/2.1.x/quickstart/).

5. Откройте браузер и введите в адресной строке:
  127.0.0.1:5000
Должна появиться надпись «It works!». Если да, то значит скорее всего всё работает.

## Настройки слоёв в JOSM

6. Запустите JOSM, выберите «Слои» → «Настройки слоёв»
В окне настроек нажмите кнопку «+ WMS»

7. В появившемся окне в пункте 6 введите ссылку в соответствии с нужным слоем (смотрите ниже),
в пункте 7 укажите название слоя (любое чтобы Вам было удобно):

Публичная кадастровая карта — Земельные участки
```
wms[20]:http://127.0.0.1:5000/path/land?bbox={bbox}
```

Публичная кадастровая карта — Здания и сооружения
```
wms[20]:http://127.0.0.1:5000/path/building?bbox={bbox}
```

Публичная кадастровая карта — Границы единиц АТД и населённых пунктов
```
wms[20]:http://127.0.0.1:5000/path/boundary?bbox={bbox}
```

Публичная кадастровая карта — Зоны и территории
```
wms[20]:http://127.0.0.1:5000/path/zone?bbox={bbox}
```

Нажмите ОК в двух окнах.

8. Теперь выберине нужный слой («Слои» → Название слоя, который вы указали в предыдущем пункте)

Всё, должно работать. Если не заработало, пишите мне, буду разбираться.

Примечание: Иногда бывает, что скачивание происходит с ошибкой. Если подождать 5-10 секунд, то JOSM должен сам повторно обратиться к пропущенному тайлу. Если этого не произошло, в окне выбора слоя нажмите правой кнопкой мыши по слою и выберите «Скачать все квадраты с ошибками».

Обычно со 2-3 раза скачиваются все квадраты.
