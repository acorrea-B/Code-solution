FROM python:3.8

ENV VIRTUAL_ENV=/points_challenge/venv

WORKDIR /points_challenge

RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ADD . /points_challenge

RUN cd /points_challenge && make install