# Basis-Image, das Python enthält
FROM python:3.8-slim

# Arbeitsverzeichnis im Container festlegen
WORKDIR /app

# Abhängigkeiten kopieren und installieren
# Zuerst 'requirements.txt' kopieren, um Caching zu nutzen, falls sich 'requirements.txt' nicht ändert
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopieren des restlichen Quellcodes in das Arbeitsverzeichnis
COPY . .

# Port freigeben, der vom Flask-Server verwendet wird
EXPOSE 8080

CMD ["python", "./app.py"]