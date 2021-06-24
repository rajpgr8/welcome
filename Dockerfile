FROM python:3.7.3-alpine
COPY requirements.txt /
RUN pip install -f requirements.txt

COPY src /app
WORKDIR /app

EXPOSE 9091

CMD ["python3", "app.py"]
