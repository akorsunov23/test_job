# Оплата товаров и заказов

### Установка и запуск приложения на локальном сервере

- установить все зависимости из пакета requirements.txt
```angular2html
pip install -r requirements.txt
```
- создать суперпользователя 'admin'
```angular2html
python manage.py createsuperuser
```
- выполнить миграции базы данных
```angular2html
python manage.py migrate
```
- запустить проект из папки с приложением
```angular2html
python manage.py runserver
```
- добавить через админ-панель "http://127.0.0.1:8000/admin/" в соответствующие модели информацию о товаре
- доступные url:
```angular2html
http://127.0.0.1:8000/item/{id}
```
Для вывода детальной информации о товаре и возможности оплатить его 
использую библиотеку Stripe.
```angular2html
http://127.0.0.1:8000/buy/{id}
```
Получение SessionID выбранного товара.
```angular2html
http://127.0.0.1:8000/order/{id}
```
Для вывода детальной информации о заказе и возможности оплатить его 
использую библиотеку Stripe.
```angular2html
http://127.0.0.1:8000/buy_order/{id}
```
Получение SessionID выбранного заказа.

### Запуск проекта на удалённом сервере