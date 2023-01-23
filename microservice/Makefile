install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black */*.py

lint:
	pylint --disable=R,C */*.py

venv: 
	python3 -m venv ./venv &&\
		source venv/bin/activate && \
		make install
test:
	python manage.py test

load:
	python manage.py loaddata db.json

run:
	python manage.py makemigrations &&\
        python manage.py migrate &&\
			make load &&\
				make test &&\
                	python manage.py runserver 0.0.0.0:8000

launch:
	docker-compose build && docker-compose up

server:
	docker exec -ti amazonas_store  bash