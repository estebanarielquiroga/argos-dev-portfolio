FROM python:3.11

RUN apt-get update && apt-get install -y curl unzip git && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs && rm -rf /var/lib/apt/lists/*

# Caddy (servidor web profesional)
RUN curl -fsSL https://github.com/caddyserver/caddy/releases/download/v2.8.4/caddy_2.8.4_linux_amd64.tar.gz \
    -o /tmp/caddy.tar.gz \
    && tar -xzf /tmp/caddy.tar.gz -C /tmp \
    && mv /tmp/caddy /usr/local/bin/caddy \
    && chmod +x /usr/local/bin/caddy \
    && rm /tmp/caddy.tar.gz

RUN curl -fsSL https://bun.sh/install | bash
ENV PATH="/root/.bun/bin:$PATH"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV REFLEX_ENV=prod
ENV NODE_ENV=production

RUN reflex init

# Script sin CRLF, usando el puerto correcto de Railway (8000)
RUN printf '#!/bin/sh\n\
PORT=${PORT:-8000}\n\
echo ">>> Iniciando en puerto $PORT"\n\
reflex export --frontend-only --no-zip\n\
echo ">>> Archivos:"\n\
ls /app/.web/build/client/ 2>/dev/null || echo "SIN ARCHIVOS"\n\
reflex run --env prod --backend-only --backend-port 8001 &\n\
sleep 3\n\
echo ">>> Caddy en $PORT"\n\
exec caddy run --config /app/Caddyfile --adapter caddyfile\n\
' > /start.sh && chmod +x /start.sh

CMD ["/start.sh"]
