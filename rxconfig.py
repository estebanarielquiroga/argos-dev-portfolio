import reflex as rx

# ============================================================
# rxconfig.py - Configuración central de la aplicación Reflex
#
# api_url: La URL donde el frontend puede encontrar al backend.
# En Railway, la variable RAILWAY_PUBLIC_DOMAIN contiene el dominio
# público (ej: argos-dev-portfolio.up.railway.app).
# ============================================================

config = rx.Config(
    app_name="argos_dev_portfolio",
    # En producción, el frontend llama al backend usando el dominio público de Railway
    api_url=f"https://{__import__('os').getenv('RAILWAY_PUBLIC_DOMAIN', 'localhost:8001')}",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)