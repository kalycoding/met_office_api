
FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /home
COPY Pipfile Pipfile.lock /home/
RUN pip install pipenv && pipenv install --system
COPY . /home/
