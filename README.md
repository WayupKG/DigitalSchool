# Инструкция по запуску проекта через virtualenv

- ### Клонирование проекта
  **Git clone** <br>
  ```
  git clone git@github.com:WayupKG/El-School.git
  cd El-School
  ```
  
- ### Установка виртуального окружения
  Убедитесь, что Python версии 3.10 и virtualenv установлен на вашем компьютере или ноутбуке.<br>
  Установка Python3 на [Windows](https://www.youtube.com/watch?v=IU4-19ofajg),
 	 <br>
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```
  

- ### Создание виртуальных переменные
  Создайте файл `.env` и заполните его как на примере `.env.dist` <br>

- ### Активация виртуального окружения
  ```
  source venv/bin/activate
  ```
  для Windows
  ```
  venv\Scripts\activate.bat
  ```

- ### Установка зависимостей
  Он установит все необходимые зависимости для проекта.<br>
  ```
  pip3 install -r requirements.txt
  ```
  
- ### Миграции 
  Для запуска миграций. <br>
  ```
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```
  
- ### Создание суперпользователя
  Для создания суперпользователя напишите команду. <br>
  ```  
  python3 manage.py createsuperuser
  ```
  После выполнения этой команды она запросит имя пользователя и пароль.
  С помощью этого аккаунта вы получите доступ к панели администратора `http://localhost:8000/admin/`

- ### Запуск проекта
  ```
  python3 manage.py runserver
  ```
   Он будет работать на порту 8000 по умолчанию.<br>

# Инструкция по запуску проекта через Docker

- ### Клонирование проекта
  **Git clone** <br>
  ```
  git clone git@github.com:WayupKG/El-School.git
  cd El-School
  ```
  
- ### Создание виртуальных переменные
  Создайте файл `.env` и заполните его как на примере `.env.dist` <br>

- ### Сборка проекта
  ```
  docker compose build
  ```
  
- ### Миграции 
  Для запуска миграций. <br>
  ```
  docker compose run --rm web-app sh -c "python3 manage.py makemigrations"
  docker compose run --rm web-app sh -c "python3 manage.py migrate"
  ```
  
- ### Создание суперпользователя
  Для создания суперпользователя напишите команду. <br>
  ```  
  docker compose run --rm web-app sh -c "python3 manage.py createsuperuser"
  ```
  После выполнения этой команды она запросит имя пользователя и пароль.
  С помощью этого аккаунта вы получите доступ к панели администратора `http://localhost:8000/admin/`

- ### Запуск проекта
  ```
  docker compose up
  ```
   Он будет работать на порту 8000 по умолчанию.<br>
