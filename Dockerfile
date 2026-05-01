# ============================================================
# Imagen base Python 3.11 completa
# ============================================================
FROM python:3.11

# Instalamos herramientas del sistema
RUN apt-get update && apt-get install -y \
    curl unzip git \
    && rm -rf /var/lib/apt/lists/*

# Instalamos Node.js 20 (requerido por Reflex)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Instalamos Caddy (servidor web para servir el frontend)
RUN curl -fsSL https://github.com/caddyserver/caddy/releases/download/v2.8.4/caddy_2.8.4_linux_amd64.tar.gz \
    -o /tmp/caddy.tar.gz \
    && tar -xzf /tmp/caddy.tar.gz -C /tmp \
    && mv /tmp/caddy /usr/local/bin/caddy \
    && chmod +x /usr/local/bin/caddy \
    && rm /tmp/caddy.tar.gz

WORKDIR /app

# Dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Codigo de la aplicacion
COPY . .

# ============================================================
# BUILD TIME: Compilar el frontend aqui para que el arranque sea rapido
# ============================================================
ENV REFLEX_ENV=prod
ENV NODE_ENV=production

RUN reflex init
RUN reflex export --frontend-only --no-zip

# Verificamos que los archivos existan (si falla aqui, el build falla tambien)
RUN ls -la /app/.web/_static/

# ============================================================
# RUNTIME: Caddy sirve el frontend + Reflex corre el backend
# Usamos un script inline para evitar problemas de CRLF en Windows
# ============================================================
CMD ["/bin/sh", "-c", "\
    echo '=== Iniciando backend Reflex en puerto 8001 ===' && \
    reflex run --env prod --backend-only --backend-port 8001 & \
    sleep 5 && \
    echo '=== Iniciando Caddy en puerto '${PORT:-8080}' ===' && \
    caddy run --config /app/Caddyfile --adapter caddyfile \
"]
