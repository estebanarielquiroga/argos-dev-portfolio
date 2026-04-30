# Usamos una imagen de Python oficial como base
FROM python:3.11-slim

# Instalamos curl para el proceso de instalación de Node.js
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

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

# Inicializamos Reflex en el servidor para preparar el frontend
RUN reflex init

# Exponemos los puertos que usa Reflex (8000 para el backend y 3000 para el frontend)
EXPOSE 8000
EXPOSE 3000

# Comando para arrancar la aplicación en modo producción
CMD ["reflex", "run", "--env", "prod", "--backend-only"]
