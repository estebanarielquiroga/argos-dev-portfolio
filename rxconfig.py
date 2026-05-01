import reflex as rx

config = rx.Config(
    app_name="argos_dev_portfolio",
    api_url="https://quirodev.ar",
    # Forzamos al backend a escuchar en todas las interfaces internas
    backend_host="0.0.0.0",
)