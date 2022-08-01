FROM python:3.10-alpine

WORKDIR /app

# COPY requirements-dev.txt requirements-dev.txt
COPY requirements.txt requirements.txt

# RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./news_be/.env .
COPY . .

RUN ln -fs /app/news_be/manage.py /app/manage.py

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]