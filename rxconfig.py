import os
import reflex as rx
from reflex.plugins import SitemapPlugin

config = rx.Config(
    app_name="argos_dev_portfolio",
    api_url=os.getenv("API_URL", "https://quirodev.ar"),
    # Usamos la clase del plugin directamente para evitar el DeprecationWarning
    disable_plugins=[SitemapPlugin],
)