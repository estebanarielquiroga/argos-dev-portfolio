import os
import reflex as rx

config = rx.Config(
    app_name="argos_dev_portfolio",
    # Usamos la variable de entorno API_URL o el dominio fijo
    api_url=os.getenv("API_URL", "https://quirodev.ar"),
)