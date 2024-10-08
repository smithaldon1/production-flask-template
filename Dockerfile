FROM python:3.10-slim-buster

RUN apt-get update \
    && apt-get install python3-dev default-libmysqlclient-dev build-essential -y

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Fix pyxb issue
# COPY lib/pyxb/binding/content.py /usr/local/lib/python3.10/site-packages/pyxb/binding/content.py

COPY . /app

CMD ["python3", "application.py"] 