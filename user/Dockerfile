FROM python:alpine3.10

WORKDIR /app

COPY . .

RUN apk add gcc musl-dev \
    && pip3 install -r requirements.txt \
    && pip install .

EXPOSE 3000

CMD ["pena", "http", "start"]