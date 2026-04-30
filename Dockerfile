# Imagen base
FROM python:3.11-slim

# Instalamos solo lo básico
RUN apt-get update && apt-get install -y \
    curl unzip git nodejs \
    && curl -sL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código
COPY . .

# Construcción
ENV REFLEX_ENV=prod
ENV NODE_ENV=production
RUN reflex init
RUN reflex export --frontend-only --no-zip

# Exponemos el puerto
EXPOSE 8080

# COMANDO SUPER SIMPLE:
# 1. Arrancamos el motor de Python de fondo.
# 2. Usamos el servidor más básico de Python para mostrar la web.
CMD ["sh", "-c", "echo '--- INICIANDO SERVIDOR EN PUERTO '$PORT' ---' && (reflex run --env prod --backend-only --backend-port 8001 &) && cd .web/_static && python3 -m http.server $PORT"]
