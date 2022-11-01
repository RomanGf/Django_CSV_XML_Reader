## 1) Створюєм віртуальне середовище
> python3 -m venv venv

## 2) Запускаєм docker-compose
> docker-compose up -d

## 3) Створюєм суперкористувача, який буде адміном 
> docker-compose run web python3 manage.py createsuperuser

## 4) Добавляєм групи через адмінку, заходим по url, використовуючи адміна, створеного в пункті 4 та переходимо на вкладку Authentication and Authorization вибираєм Group і створюєм 2 групи

> http://0.0.0.0:8000/admin/

### Групи:
> admin

> user

## 5) В Authentication and Authorization вибираєм User і знаходимо адміна, якого створили в 4 пункті. Міняємо в нього настройки групи, та присвоюємо групу:
> admin