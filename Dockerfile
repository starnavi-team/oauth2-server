FROM python:3.6
RUN mkdir -p /data/code
WORKDIR /data/code
ADD requirements.txt /data/code/
RUN pip install uwsgi --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir
ADD . /data/code/
