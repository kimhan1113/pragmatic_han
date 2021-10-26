FROM python:3.9.0

ARG DISABLE_CACHE

WORKDIR /home/

RUN echo "testing123123"

RUN git clone https://github.com/kimhan1113/pragmatic_han.git

RUN ls -al

WORKDIR /home/pragmatic_han/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=pragmatic.settings.deploy \
&& python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]

RUN ls -al

