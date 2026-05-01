FROM python:3.11

RUN apt-get update && apt-get install -y curl unzip git && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs && rm -rf /var/lib/apt/lists/*

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

# Script de arranque inteligente
RUN printf '#!/bin/sh\n\
PORT=${PORT:-8000}\n\
echo ">>> Migrando Base de Datos..."\n\
reflex db migrate || echo "Sin migraciones necesarias"\n\
echo ">>> Iniciando Backend..."\n\
reflex run --env prod --backend-only --backend-port $REFLEX_BACKEND_PORT > backend.log 2>&1 &\n\
\n\
echo ">>> Esperando a que el Backend responda en $REFLEX_BACKEND_PORT..."\n\
n=0\n\
until [ $n -ge 20 ] || curl -s http://127.0.0.1:$REFLEX_BACKEND_PORT/ping > /dev/null; do\n\
  echo ">>> Todavia esperando al backend..."\n\
  sleep 2\n\
  n=$((n+1))\n\
done\n\
\n\
if [ $n -ge 20 ]; then\n\
  echo ">>> ERROR: El backend no arranco a tiempo. Ultimas lineas del log:"\n\
  tail -n 20 backend.log\n\
  exit 1\n\
fi\n\
\n\
echo ">>> Backend listo. Iniciando Caddy en puerto $PORT..."\n\
exec caddy run --config /app/Caddyfile --adapter caddyfile\n\
' > /start.sh && chmod +x /start.sh

CMD ["/start.sh"]
