#!/bin/sh
# ============================================================
# entrypoint.sh - Orquestador de arranque de la aplicación
# Ejecuta el backend de Reflex (puerto interno 8001)
# y Caddy (sirve el frontend en el $PORT que Railway asigna)
# ============================================================

set -e

echo "=============================================="
echo "  INICIANDO ARGOS-DEV PORTFOLIO"
echo "  Puerto público (Railway): ${PORT:-8080}"
echo "  Puerto interno backend:   8001"
echo "=============================================="

# Arrancamos el backend de Reflex en segundo plano (puerto interno 8001)
echo ">> Arrancando backend Reflex en puerto 8001..."
reflex run --env prod --backend-only --backend-port 8001 &

# Esperamos unos segundos para que el backend esté listo
sleep 5

# Arrancamos Caddy en el puerto que Railway nos asigna ($PORT)
echo ">> Arrancando Caddy en puerto ${PORT:-8080}..."
exec caddy run --config /app/Caddyfile --adapter caddyfile
