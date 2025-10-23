# Homework 2: Firefox Screenshot Test

## Описание задания
Автоматизация браузера Firefox с использованием Selenium WebDriver и Pytest для создания скриншотов веб-страниц.

## Файлы в папке
- `test_firefox_screenshot.py` — основной скрипт с тестом для создания скриншота  
- `payment_methods.png` — скриншот, созданный после выполнения теста  
- `README.md` — это описание

## Как запустить тест
```bash
pytest test_firefox_screenshot.py -v

Цель:
Написать автоматизированный тест для создания скриншота раздела "Способы оплаты" на сайте https://itcareerhub.de/ru

Функциональность теста:
Автоматическое открытие браузера Firefox
Переход на страницу https://itcareerhub.de/ru
Навигация в раздел "Способы оплаты"
Создание скриншота страницы
Автоматическое закрытие браузера после теста
После выполнения теста в папке проекта появится файл payment_methods.png — скриншот целевой страницы

Требования к окружению:

Python 3.6+
Установленный браузер Firefox

Библиотеки:
selenium
webdriver-manager
pytest

Установка зависимостей:
pip install selenium webdriver-manager pytest


