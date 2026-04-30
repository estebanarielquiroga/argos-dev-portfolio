# Imagen base
FROM python:3.11-slim

# Instalamos lo necesario
RUN apt-get update && apt-get install -y \
    curl unzip git \
    && curl -sL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY . .

# Variables de entorno
ENV REFLEX_ENV=prod
ENV NODE_ENV=production

# --- CONSTRUCCIÓN FORZADA ---
# Inicializamos y exportamos a una carpeta que SABEMOS que existirá
RUN reflex init
RUN reflex export --frontend-only --no-zip

# Exponemos el puerto
EXPOSE 8080

# COMANDO FINAL:
# Buscamos dónde quedó la web y la servimos
CMD ["sh", "-c", "(reflex run --env prod --backend-only --backend-port 8001 &) && python3 -m http.server $PORT --directory .web/_static"]
