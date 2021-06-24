FROM python:3.7.3-alpine
COPY requirements.txt /
RUN apt-get update && \
    apt-get install python3-venv -y \
    && pip3 install -r /requirements.txt

COPY src /app
WORKDIR /app

EXPOSE 9091

CMD ["python3", "app.py"]
