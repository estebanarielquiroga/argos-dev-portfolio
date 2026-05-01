import reflex as rx

config = rx.Config(
    app_name="argos_dev_portfolio",
    api_url="https://quirodev.ar",
    # Usamos 127.0.0.1 para comunicacion interna super segura con Caddy
    backend_host="127.0.0.1",
)