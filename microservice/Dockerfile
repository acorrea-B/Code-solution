FROM python:3.8

ENV PYTHONUNBUFFERED 1

ENV VIRTUAL_ENV=/points_challenge/venv

WORKDIR /store_juanita

RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy the current directory contents into the container at /store_juanita
ADD . /store_juanita

# Install any needed packages specified in requirements/dev.txt
RUN cd /store_juanita && make install