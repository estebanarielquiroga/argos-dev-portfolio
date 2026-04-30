# Imagen base de Python
FROM python:3.11-slim

# Instalamos herramientas básicas del sistema
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    git \
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
EXPOSE 8000

# Comando final: inicializa, exporta y arranca el backend
CMD ["sh", "-c", "reflex init && reflex export --frontend-only --no-zip && reflex run --env prod --backend-only --backend-port ${PORT:-8000}"]
