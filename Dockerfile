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

RUN reflex init

# Script de arranque con LF garantizado
RUN printf '#!/bin/sh\n\
PORT=${PORT:-8080}\n\
echo "PORT=[$PORT]"\n\
echo "Exportando frontend..."\n\
reflex export --frontend-only --no-zip\n\
echo "Iniciando backend en 8001..."\n\
reflex run --env prod --backend-only --backend-port 8001 &\n\
sleep 3\n\
echo "Iniciando servidor HTTP en $PORT..."\n\
cd /app/.web/build/client && python3 -m http.server $PORT\n\
' > /start.sh && chmod +x /start.sh

CMD ["/start.sh"]
