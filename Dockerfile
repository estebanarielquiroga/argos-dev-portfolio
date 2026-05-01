FROM python:3.11

# Instalacion de dependencias de sistema y CADDY
RUN apt-get update && apt-get install -y curl unzip git debian-keyring debian-archive-keyring apt-transport-https \
    && curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg \
    && curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list \
    && apt-get update && apt-get install -y caddy \
    && rm -rf /var/lib/apt/lists/*

# Instalacion de Bun (necesario para el frontend de Reflex)
RUN curl -fsSL https://bun.sh/install | bash
ENV PATH="/root/.bun/bin:$PATH"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV REFLEX_ENV=prod
ENV NODE_ENV=production
ENV API_URL=https://quirodev.ar
ENV REFLEX_BACKEND_PORT=8001

# Build time export
RUN reflex init
RUN reflex export --frontend-only --no-zip

# Script de arranque refinado
RUN printf '#!/bin/sh\n\
PORT=${PORT:-8000}\n\
echo ">>> Iniciando Backend..."\n\
reflex run --env prod --backend-only --backend-port $REFLEX_BACKEND_PORT > backend.log 2>&1 &\n\
\n\
echo ">>> Esperando al backend..."\n\
sleep 15\n\
\n\
echo ">>> Iniciando Caddy en puerto $PORT..."\n\
exec caddy run --config /app/Caddyfile --adapter caddyfile\n\
' > /start.sh && chmod +x /start.sh

CMD ["/start.sh"]
