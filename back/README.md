# BACKEND

## Запуск проекта на flask (app.py)
```bash
$ flask run
# or
$ python -m flask run
# or
$ python3 -m flask run
```


## Структура проекта
### activate VENV
```bash
$ . ./init.sh
```

### stop VENV
```bash
$ deactivate
```

#### Структура проекта
```
src
 |-- bp_component   # нициализации/подключения
 |-- models         # база данных
 |-- static         # статические данные
 |-- lib            # подключения библиотек
 |-- config         # глобальные параметры
 |-- data           # данные подгружаемые в процессе работы + логи
 |-- data           # данные подгружаемые в процессе работы + логи
 |-- utils          # скрипты
 |__ ...
```


models
Модель БД

static
Здесь все основные никогда не меняющиеся (или меняющиеся крайне редко) стили, картинки, звуки, JS библиотеки и фреймворки.

lib
Например у меня лежат некоторые функции-декораторы, при обработке маршрута, но до вызова основной функции.

config
Как хранить настройки, определяющие глобальные параметры приложения? Сколько на этот счет было баталий и не счесть. Без деталей как делаю я: храню в виде Python модуля отдельным каталогом. Внутри файлы для разных режимов запуска.

data
Подгружаемые в процессе работы файлы, логи и другие данные хранятся в отдельном каталоге data

logs
Сюда можно складывать логи при тестовых запусках или выводы самого приложения.

utils
Вспомогательные скрипты и утилиты

https://habr.com/ru/articles/421887/

https://the-bosha.ru/2016/06/03/python-flask-freimvork-pravilnaia-struktura-prilozheniia/