pip install -r requirements.txt
cd BackendPixieTech
python manage.py collectstatic
python manage.py migrate
