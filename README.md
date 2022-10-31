## 1) Створюєм віртуальне середовище
> python3 -m venv venv

## 2) Встановлюєм залежності
> pip3 install -r requirements.txt


## 3) Виконуєм міграції
>python3 manage.py makemigrations 


>python3 manage.py migrate
## 4) Створюєм адміна за допомогою команди

>python3 manage.py createsuperuser

## 5) Добавляєм групи через адмінку, заходим по url, використовуючи адміна, створеного в пункті 4 та переходимо на вкладку Authentication and Authorization вибираєм Group і створюєм 2 групи
> http://localhost:8000/admin/

### Групи:
> admin

> user

## 6) В Authentication and Authorization  вибираєм User і знаходимо адміна, якого створили в 4 пункті. Міняємо в нього настройки групи, та присвоюємо групу:
> admin

## Запускаємо проект

>python3 manage.py runserver