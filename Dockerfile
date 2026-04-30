# Imagen base de Python
FROM python:3.11-slim

# Instalamos herramientas básicas y Caddy (Servidor web profesional)
RUN apt-get update && apt-get install -y \
    curl unzip git debian-keyring debian-archive-keyring apt-transport-https \
    && curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg \
    && curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list \
    && apt-get update && apt-get install -y caddy \
    && rm -rf /var/lib/apt/lists/*

# Instalamos Node.js
RUN curl -sL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

# Directorio de trabajo
WORKDIR /app

# Instalamos dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY . .

# Variables de entorno
ENV REFLEX_ENV=prod
ENV NODE_ENV=production

# Exponemos el puerto
EXPOSE 8080

# Comando final:
# 1. Preparamos la web (init y export)
# 2. Arrancamos el motor de Python de fondo (puerto 8001)
# 3. Arrancamos Caddy al frente para que maneje todo (puerto asignado por Railway)
CMD ["sh", "-c", "reflex init && reflex export --frontend-only --no-zip && (reflex run --env prod --backend-only --backend-port 8001 &) && caddy run --config Caddyfile --adapter caddyfile"]
