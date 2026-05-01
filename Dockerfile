FROM python:3.11

RUN apt-get update && apt-get install -y \
    curl unzip git \
    && rm -rf /var/lib/apt/lists/*

# Node.js 20
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Caddy
RUN curl -fsSL https://github.com/caddyserver/caddy/releases/download/v2.8.4/caddy_2.8.4_linux_amd64.tar.gz \
    -o /tmp/caddy.tar.gz \
    && tar -xzf /tmp/caddy.tar.gz -C /tmp \
    && mv /tmp/caddy /usr/local/bin/caddy \
    && chmod +x /usr/local/bin/caddy \
    && rm /tmp/caddy.tar.gz

# Bun
RUN curl -fsSL https://bun.sh/install | bash
ENV PATH="/root/.bun/bin:$PATH"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV REFLEX_ENV=prod
ENV NODE_ENV=production

# Inicializamos en build time (instala node_modules, configura .web/)
RUN reflex init

# Creamos el script de arranque usando printf (garantiza LF, no CRLF)
RUN printf '#!/bin/sh\n\
set -e\n\
\n\
PORT=${PORT:-8080}\n\
echo ">>> Arrancando en puerto $PORT"\n\
\n\
echo ">>> Exportando frontend..."\n\
reflex export --frontend-only --no-zip\n\
\n\
echo ">>> Archivos creados:"\n\
find /app/.web -name "*.html" 2>/dev/null | head -10 || echo "SIN HTML"\n\
\n\
echo ">>> Iniciando backend Reflex en 8001..."\n\
reflex run --env prod --backend-only --backend-port 8001 &\n\
\n\
sleep 5\n\
echo ">>> Iniciando Caddy en $PORT..."\n\
exec caddy run --config /app/Caddyfile --adapter caddyfile\n\
' > /start.sh && chmod +x /start.sh

CMD ["/start.sh"]
