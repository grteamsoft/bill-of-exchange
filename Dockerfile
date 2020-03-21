FROM python:3.8.2

WORKDIR /app

RUN pip install -U pip
RUN pip install -U aiogram
RUN pip install -U psycopg2 

# CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"

ENTRYPOINT ["bin/start_dev.sh"]
