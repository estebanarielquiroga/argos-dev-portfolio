# Imagen base (Usamos una más completa para Render)
FROM python:3.11

# Instalamos herramientas
RUN apt-get update && apt-get install -y \
    curl unzip git nodejs npm \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código
COPY . .

# Construcción
ENV REFLEX_ENV=prod
ENV NODE_ENV=production
RUN reflex init
RUN reflex export --frontend-only --no-zip

# Render usa la variable PORT automáticamente
# Usamos el motor de Reflex para servir todo
CMD ["sh", "-c", "reflex run --env prod --backend-only --backend-port $PORT"]
