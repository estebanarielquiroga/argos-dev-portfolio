# Usamos una imagen de Python oficial como base
FROM python:3.11-slim

# Instalamos curl y unzip para el proceso de instalación de Node.js y Bun
RUN apt-get update && apt-get install -y curl unzip && rm -rf /var/lib/apt/lists/*

# Instalamos Node.js (necesario para el frontend de Reflex)
RUN curl -sL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

# Seteamos el directorio de trabajo
WORKDIR /app

# Copiamos el archivo de requerimientos e instalamos las librerías de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el proyecto al servidor
COPY . .

# Seteamos variables de entorno para producción
ENV NODE_ENV=production
ENV REFLEX_ENV=prod

# Inicializamos y exportamos el frontend (esto genera los archivos estáticos)
RUN reflex init
RUN reflex export --frontend-only --no-zip

# Exponemos el puerto (Railway usa la variable PORT dinámicamente)
# No es necesario EXPOSE fijo, pero usaremos 8000 como backup
EXPOSE 8000

# Usamos un shell para que la variable $PORT se expanda correctamente
CMD ["sh", "-c", "reflex run --env prod --backend-only --backend-port ${PORT:-8000} --loglevel debug"]
