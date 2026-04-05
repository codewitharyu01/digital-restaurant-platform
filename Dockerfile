# 1. Python image use karein
FROM python:3.10-slim

# 2. Build tools install karein (agar psycopg2 jaisi libraries hon)
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# 3. Working directory set karein
WORKDIR /app

# 4. Saari files copy karein
COPY . .

# 5. Pip upgrade aur requirements install karein
# Hum folder ke andar jaakar install karenge kyunki aapki files 'myrestu' mein hain
RUN pip install --upgrade pip
RUN cd myrestu && pip install -r requirements.txt

# 6. Static files collect karein
RUN cd myrestu && python manage.py collectstatic --noinput

# 7. Server start karein
EXPOSE 8000
CMD ["sh", "-c", "cd myrestu && gunicorn myrestu.wsgi --bind 0.0.0.0:${PORT:-8080}"]