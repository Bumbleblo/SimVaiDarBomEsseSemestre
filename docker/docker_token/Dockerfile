FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /home

COPY docker/docker_token/requirements.txt .

RUN pip3 install --no-cache -r requirements.txt

COPY main.py .

ENTRYPOINT ["python3", "main.py"]
