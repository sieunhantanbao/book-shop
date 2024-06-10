FROM python:3.11.4-slim-buster
# build variables.
ENV DEBIAN_FRONTEND noninteractive

# Set working directory
WORKDIR /app

RUN apt-get update -y && apt-get update

# Install app dependencies
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# clean the install.
RUN apt-get -y clean
# copy all files to /app directory and move into directory.

# Bundle app source
COPY . /app

COPY wait /app
# Script to wait for PostgreSQL
RUN ["chmod", "+x", "/app/wait"]

EXPOSE 8000

# CMD ["uvicorn", "app.main:app","--host","0.0.0.0","--port","8000"]
