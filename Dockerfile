# Imagen base
FROM python:3.11-slim

WORKDIR /app

# Solo instalamos lo básico para el motor de Python
RUN apt-get update && apt-get install -y \
    curl unzip git \
    && rm -rf /var/lib/apt/lists/*

# Instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos TODO (incluyendo la carpeta .web que vas a subir)
COPY . .

# Variables de entorno
ENV REFLEX_ENV=prod

# COMANDO FINAL:
# Arrancamos el motor y servimos la carpeta que YA SUBISTE
CMD ["sh", "-c", "(reflex run --env prod --backend-only --backend-port 8001 &) && python3 -m http.server $PORT --directory .web/build/client"]
