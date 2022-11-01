## 1) Запускаєм  docker-compose
> docker-compose up
## 2) Створюєм адміна за допомогою команди

>docker-compose run web python3 manage.py createsuperuser

## 3) Добавляєм групи через адмінку, заходим по url, використовуючи адміна, створеного в пункті 2 та переходимо на вкладку Authentication and Authorization вибираємо Groups і створюєм 2 групи
> http://localhost:8000/admin/

### Групи:
> admin (та присвоюємо йому всі пермішени)

> user

## 4) В Authentication and Authorization  вибираєм Users і знаходимо адміна, якого створили в 2 пункті. Міняємо в нього настройки групи, та присвоюємо групу:
> admin

