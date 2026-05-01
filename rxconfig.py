import reflex as rx

config = rx.Config(
    app_name="argos_dev_portfolio",
    api_url="https://quirodev.ar",
    # Desactivamos el plugin de sitemap que causa advertencias
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
)