# Imagen base
FROM python:3.11-slim

# Instalamos todo lo necesario (incluyendo Caddy)
RUN apt-get update && apt-get install -y \
    curl unzip git debian-keyring debian-archive-keyring apt-transport-https \
    && curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg \
    && curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list \
    && apt-get update && apt-get install -y caddy nodejs \
    && curl -sL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY . .

# --- CONSTRUCCIÓN EN TIEMPO DE BUILD ---
# Esto hace que el contenedor arranque INSTANTÁNEAMENTE
ENV REFLEX_ENV=prod
ENV NODE_ENV=production
RUN reflex init
RUN reflex export --frontend-only --no-zip

# Exponemos el puerto
EXPOSE 8080

# Comando de arranque: Solo encender el backend y Caddy
CMD ["sh", "-c", "(reflex run --env prod --backend-only --backend-port 8001 &) && caddy run --config Caddyfile --adapter caddyfile"]
