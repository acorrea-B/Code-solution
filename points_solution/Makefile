install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

venv: 
	python3 -m venv ./venv &&\
		source venv/bin/activate && \
		make install

format:
	black */*.py

lint:
	pylint --disable=R,C */*.py

test:
	python -m pytest -vv --capture=sys --capture=fd */test_*.py
