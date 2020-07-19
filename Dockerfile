FROM python:3.8-slim    
RUN apt update
RUN apt install libpq-dev gcc -y
RUN pip install pipenv
RUN mkdir backend
COPY . /backend
WORKDIR /backend
RUN pipenv install