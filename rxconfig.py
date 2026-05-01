import os
import reflex as rx

config = rx.Config(
    app_name="argos_dev_portfolio",
    api_url=os.getenv("API_URL", "https://quirodev.ar"),
    # Desactivamos explicitamente el plugin de sitemap para evitar advertencias y errores de build
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
)