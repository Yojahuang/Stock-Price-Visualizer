FROM python:3.10.2-alpine3.15

WORKDIR /usr/src/app

COPY . .

RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache curl
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

EXPOSE 5000
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
