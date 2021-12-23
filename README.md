# Обрезка ссылок с помощью Битли

Сокращение ссылок с помощью сервиса bit.ly и вывод статистики по переходам.

* При вводе в программу сокращённой ссылки, выведется сумма кликов по ней.
* Если же ввести длинную ссылку, то выведется сокращённая вида `http://bit.ly/XXXXXX`

Скрипт показывает переходы за все дни, а не только за текущий день.

Скрипт работает как с HTTP, так и с HTTPS ссылками.

### Как установить

Скачиваем файлы в отдельную папку.

В этой же папке создаем `.env` файл. Ваш `.env` должен содержать строку:
```commandline
BITLY_APIKEY={ВАШ КЛЮЧ API ДЛЯ BITLY}
```
Для работы программы необходимо получить персональный ключ для взаимодействия с API Bitly.

Выглядит примерно так: `11a09b87cde6543205123ac1977542fecf00231abc`

[Документации Bitly](https://dev.bitly.com/get_started.html)

[Генератор токенов](https://bitly.com/a/oauth_apps)

`GENERIC ACCESS TOKEN` — нужный тип токена


Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Использование

Используем консольный ввод.

Создать короткую ссылку битли:
```
python3 main.py https://example.com/

Битлинк: http://bit.ly/1a2B3c4
```
Вывести количество переходов по кликам по битли-ссылке:
```
python3 main.py http://bit.ly/1a2B3c4

По Вашей ссылке перешли: 3 раз(а)
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
