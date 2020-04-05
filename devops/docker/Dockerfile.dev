FROM python:3.8.2

WORKDIR /app

COPY ./requirements.txt /install/requirements.txt
RUN pip install -r /install/requirements.txt

ENTRYPOINT ["bin/start_dev.sh"]
