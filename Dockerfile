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

# ============================================================
# BUILD TIME (Compilacion): Cocinamos la pagina aqui
# ============================================================
RUN reflex init
RUN reflex export --frontend-only --no-zip

# ============================================================
# RUNTIME (Arranque): Solo iniciamos los servidores
# ============================================================
RUN printf '#!/bin/sh\n\
PORT=${PORT:-8000}\n\
export REFLEX_BACKEND_PORT=8001\n\
echo ">>> Iniciando Backend..."\n\
reflex run --env prod --backend-only --port $REFLEX_BACKEND_PORT &\n\
sleep 10\n\
echo ">>> Iniciando Caddy en $PORT..."\n\
caddy run --config /app/Caddyfile --adapter caddyfile\n\
' > /start.sh && chmod +x /start.sh

CMD ["/start.sh"]
