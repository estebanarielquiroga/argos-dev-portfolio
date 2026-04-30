import reflex as rx

config = rx.Config(
    app_name="argos_dev_portfolio",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)