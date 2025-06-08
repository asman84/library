# Base image sifatida Python 3.10 ishlatamiz
FROM python:3.12

# Ishchi katalogni yaratamiz
WORKDIR /app

RUN mkdir -p /var/log/library
# Django va boshqa bog‘liqliklar uchun requirements.txt ni ko‘chirib olamiz
COPY ./requirements.txt .

# Bog‘liqliklarni o‘rnatamiz
RUN pip install --no-cache-dir -r requirements.txt

# Loyihani ichiga ko‘chirib olamiz
COPY . .

# Django static fayllarni to‘plab qo‘yamiz
RUN python manage.py collectstatic --noinput

# Port ochamiz
EXPOSE 8000

# Django serverni ishga tushiramiz
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "upwork1.wsgi:application"]
