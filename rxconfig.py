import os
import reflex as rx

config = rx.Config(
    app_name="argos_dev_portfolio",
    api_url=f"https://{os.getenv('RAILWAY_PUBLIC_DOMAIN', 'localhost:8080')}",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)