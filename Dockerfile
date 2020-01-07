FROM python:3.8

WORKDIR /home

RUN pip install -U pip
RUN pip install -U aiogram
RUN apt-get update

# CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"

ENTRYPOINT ["python", "app/server.py"]
