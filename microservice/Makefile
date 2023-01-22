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