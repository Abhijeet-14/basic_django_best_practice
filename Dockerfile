FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./basic/.env .
COPY . .

RUN ln -fs /app/basic/manage.py /app/manage.py

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]