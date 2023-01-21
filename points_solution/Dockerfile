FROM python:3.8

ENV VIRTUAL_ENV=/points_challenge/venv

RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ADD . /points_challeng

RUN cd /points_challeng && make install && make test