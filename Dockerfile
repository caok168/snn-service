FROM python:3.6.12
LABEL maintainer="kai.cao"

ENV PIP_INDEX_URL=https://pypi.doubanio.com/simple
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/


EXPOSE 5002
#ENTRYPOINT ["python", "server.py"]
ENTRYPOINT ["gunicorn", "server:app"]
CMD ["-c", "gunicorn_conf.py", "-k", "gevent"]