
# Points solutions

En esta carpeta encontrarás la solución de los puntos 1 al 4.

Como se muestra en la siguiente estructura:

## Features

- Complex numbers
- count words
- Date and hours
- Group objects

## Tree

```bash
      .
    ├── complex_numbers
    │   ├── complejo.py
    │   ├── __init__.py
    │   └── test_complex_number.py
    ├── count_words
    │   ├── __init__.py
    │   ├── test_count_words.py
    │   ├── words.py
    │   ├── words.txt
    │   └── wrong_format.txt
    ├── date_and_hours
    │   ├── dates_and_hours.py
    │   └── test_dates_and_hours.py
    ├── Dockerfile
    ├── group_objects
    │   ├── product.py
    │   └── test_product.py
    ├── __init__.py
    ├── Makefile
    ├── pyvenv.cfg
    ├── README.md
    └── requirements.txt
```


## Run Locally

You can run this project in docker for more ease in case you don't have docker you can run the virtual env

Clone the project

```bash
  git clone https://github.com/acorrea-B/Code-solution.git
```

Go to the project directory

```bash
  cd Code-solution/points_solution/
```

Build docker

```bash
  docker build -t point_solutions .
```

Attach container

```bash
  docker run -it point_solutions bash
```

If not docker 

```bash
  cd Code-solution/points_solution/
```

Mount virtual env

```bash
  make venv
```
## Running Tests

To run tests, run the following command

```bash
  make test
```

