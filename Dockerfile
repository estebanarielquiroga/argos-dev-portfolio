# ============================================================
# Imagen base con Python 3.11 completo (no slim)
# Usamos la imagen completa para evitar problemas con herramientas de compilación
# ============================================================
FROM python:3.11

# Instalamos herramientas del sistema necesarias
RUN apt-get update && apt-get install -y \
    curl unzip git \
    && rm -rf /var/lib/apt/lists/*

# Instalamos Node.js 20 (versión requerida por Reflex)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Instalamos Caddy (servidor web profesional para servir el frontend)
RUN curl -fsSL https://github.com/caddyserver/caddy/releases/download/v2.8.4/caddy_2.8.4_linux_amd64.tar.gz \
    | tar xzf - caddy \
    && mv caddy /usr/local/bin/caddy \
    && chmod +x /usr/local/bin/caddy

WORKDIR /app

# Copiamos e instalamos dependencias de Python primero (para aprovechar caché de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código de la aplicación
COPY . .

# ============================================================
# FASE DE CONSTRUCCIÓN (Build Time):
# Compilamos el frontend aquí para que el arranque sea instantáneo
# ============================================================
ENV REFLEX_ENV=prod
ENV NODE_ENV=production

# Inicializamos Reflex (descarga Bun y configura el proyecto)
RUN reflex init

# Exportamos el frontend compilado a .web/_static
RUN reflex export --frontend-only --no-zip

# Verificamos que los archivos existan (falla el build si no hay nada)
RUN ls -la .web/_static/

# ============================================================
# ARRANQUE (Runtime):
# Caddy sirve el frontend (puerto $PORT de Railway)
# Reflex corre el backend en puerto interno 8001
# ============================================================
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
