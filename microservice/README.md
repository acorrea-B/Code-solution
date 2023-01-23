
# Amazonas store

In this folder you will find the a microservice to amazon store.

As shown in the following structure:

## Features

- Client
- Location
- Store


## Run Locally

You can run this project in docker for more ease in case you don't have docker you can run the virtual env

Clone the project

```bash
  git clone https://github.com/acorrea-B/Code-solution.git
```

Go to the project directory

```bash
  cd Code-solution/microservice/
```

Run project

```bash
  make launch
```

This launchserver and can acces by
```bash
    http://localhost:8000/
```

Attach container

```bash
  make server
```

## Running Tests

To run tests, run the following command in docker bash

```bash
  make test
```

## Swagger

[Documentation](http://localhost:8000/api/v1/swagger/)

