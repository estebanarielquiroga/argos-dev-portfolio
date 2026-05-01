import os
import reflex as rx

# Usamos el dominio personalizado como prioridad, luego el de Railway, y por ultimo localhost
domain = os.getenv('PUBLIC_DOMAIN', os.getenv('RAILWAY_PUBLIC_DOMAIN', 'quirodev.ar'))

config = rx.Config(
    app_name="argos_dev_portfolio",
    # Aseguramos que use HTTPS siempre en produccion
    api_url=f"https://{domain}",
)