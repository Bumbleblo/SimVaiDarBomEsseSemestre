FROM python:3.6-alpine

WORKDIR /home

ENV PYTHONUNBUFFERED 1

COPY docker/requirements.txt .

RUN pip3 install --no-cache -r requirements.txt && rm requirements.txt

COPY app/ .

ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0:8080"]
