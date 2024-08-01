# Задание 1: "Unit testing" тестирование  на курсе "Автоматизатор тестирования на Python" | Diplom_1

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `bun_test.py`, `burger_test.py` и т.д.

### Запуск автотестов

### Установить зависимости
``` shell
pip install -r requirements.txt
```
### Запустить все тесты
```shell
pytest -v 
```
### Оценка покрытия
```shell
pytest --cov=tests
```
### Подробная оценка покрытия, после запуска смотреть файл [index.html](htmlcov/index.html)
```shell
pytest --cov=tests --cov-report=html
```