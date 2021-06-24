FROM python:3.8-alpine
COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY src /app
WORKDIR /app

EXPOSE 9091

CMD ["python3", "app.py"]
