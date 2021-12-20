FROM python:3.9

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8085

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8085
