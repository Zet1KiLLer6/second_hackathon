FROM python:3.10.12-slim-buster
LABEL authors="ibral"

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./entry.sh .

COPY . .

ENTRYPOINT ["/usr/src/app/entry.sh"]
#CMD ["/usr/src/app/entry.sh"]