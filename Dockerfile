# ============================================================
# Imagen base Python 3.11
# ============================================================
FROM python:3.11

# Herramientas del sistema
RUN apt-get update && apt-get install -y \
    curl unzip git \
    && rm -rf /var/lib/apt/lists/*

# Node.js 20
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Caddy (servidor web)
RUN curl -fsSL https://github.com/caddyserver/caddy/releases/download/v2.8.4/caddy_2.8.4_linux_amd64.tar.gz \
    -o /tmp/caddy.tar.gz \
    && tar -xzf /tmp/caddy.tar.gz -C /tmp \
    && mv /tmp/caddy /usr/local/bin/caddy \
    && chmod +x /usr/local/bin/caddy \
    && rm /tmp/caddy.tar.gz

# Instalamos Bun EXPLICITAMENTE para que Reflex lo encuentre
RUN curl -fsSL https://bun.sh/install | bash
ENV PATH="/root/.bun/bin:$PATH"

WORKDIR /app

# Dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Codigo de la aplicacion
COPY . .

# Variables de entorno para produccion
ENV REFLEX_ENV=prod
ENV NODE_ENV=production

# ============================================================
# BUILD TIME: Inicializar y compilar frontend
# ============================================================

# Inicializamos (Bun ya esta en PATH, no necesita descargarlo)
RUN reflex init

# Exportamos el frontend y mostramos donde quedaron los archivos
RUN reflex export --frontend-only --no-zip
RUN echo "=== Archivos HTML generados ===" && find /app -name "*.html" -type f 2>/dev/null | head -20 || echo "SIN HTML"
RUN echo "=== Contenido de .web ===" && ls -la /app/.web/ 2>/dev/null || echo "Sin carpeta .web"

# ============================================================
# RUNTIME: Caddy + backend Reflex
# ============================================================
CMD ["/bin/sh", "-c", "\
    echo '=== PUERTO RAILWAY: '${PORT:-8080}' ===' && \
    reflex run --env prod --backend-only --backend-port 8001 & \
    sleep 5 && \
    caddy run --config /app/Caddyfile --adapter caddyfile \
"]
