# pusto-studio
 Модель игрока и его бустов / Присвоение игроку приза за прохождение уровня. Выгрузка информации в csv

### Запуск проекта
Для Windows:

```shell
git clone https://github.com/pasha-danilevich/pusto-studio.git
python -m venv env
venv/Scripts/activate
python -m pip install --upgrade pip
cd src
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

Для корректной работы приложения необходимо:
 * сгенерировать записи
```shell
python manage.py generate_test_data
```
Запустить сервер разработки
```shell
python manage.py runserver
```
* откройте сайт
1. Присвоение игроку приза за прохождение уровня.
   
```http://127.0.0.1:8000/player/assign-prize/<int:player_id>/<int:level_id>/```

3. Выгрузка в csv данных

```http://127.0.0.1:8000/player/export/player-levels/```
