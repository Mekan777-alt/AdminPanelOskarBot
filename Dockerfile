FROM python:3.10-slim AS django-static-builder

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . .

ENV DJANGO_SETTINGS_MODULE=admin.settings
ENV DEBUG=False

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "admin.wsgi:application", "--workers", "3", "--bind", "0.0.0.0:8000"]