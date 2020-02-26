FROM python:3.8
WORKDIR /srv/api
RUN pip install pipenv
RUN pip install uwsgi
ADD backend/Pipfile* /srv/api/
RUN pipenv install --system
ADD backend/. /srv/api
ADD docker/django_server/settings.py /srv/api/backend/.
CMD ["python", "-V"]
