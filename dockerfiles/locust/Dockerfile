FROM python:3.10-slim

WORKDIR /locust

COPY ./locust/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./locust/locustfile.py locustfile.py

EXPOSE 8089

CMD ["locust"]
