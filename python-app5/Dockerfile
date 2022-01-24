FROM python:3.8

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
COPY app.py /app/

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD python3 app.py
