FROM python:3.7

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN chmod u+x ./run.sh
ENTRYPOINT ["./run.sh"]
