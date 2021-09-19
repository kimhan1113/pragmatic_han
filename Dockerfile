FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/kimhan1113/pragmatic_han.git

WORKDIR /home/pragmatic/

RUN ls -al

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-v*t(-bbuxtjn_wb&(j2x&^%=$xjvg)r8h-^%=zih)v#$q(%i0k" > .env

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]