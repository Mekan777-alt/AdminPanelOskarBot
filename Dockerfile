FROM python:3.10-slim AS django-static-builder

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .


ENV DJANGO_SETTINGS_MODULE=admin.settings
ENV DEBUG=False


RUN python manage.py collectstatic --noinput


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--insecure"]
