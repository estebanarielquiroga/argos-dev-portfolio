import os
import reflex as rx

config = rx.Config(
    app_name="argos_dev_portfolio",
    # Priorizamos la variable de entorno API_URL inyectada en el build/runtime
    api_url=os.getenv("API_URL", "https://quirodev.ar"),
)