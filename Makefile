super = false

make:
	python manage.py makemigrations
	python manage.py migrate
ifeq ($(super), true)
	python manage.py createsuperuser
endif

run:
	python manage.py runserver

reset_db: db.sqlite3
	mv app/migrations/__init__.py make_temp.py
	rm -r app/migrations/*
	mv make_temp.py app/migrations/__init__.py
	rm db.sqlite3