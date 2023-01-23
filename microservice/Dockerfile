FROM python:3.8

ENV PYTHONUNBUFFERED 1

ENV VIRTUAL_ENV=/points_challenge/venv

WORKDIR /amazonas_store

RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy the current directory contents into the container at /amazonas_store
ADD . /amazonas_store

# Install any needed packages specified in requirements/dev.txt
RUN cd /amazonas_store && make install