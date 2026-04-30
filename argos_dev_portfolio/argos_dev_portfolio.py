import reflex as rx

from .styles.styles import BASE_STYLE
from .components.hero import hero
from .components.about import about
from .components.services import services
from .components.projects import projects
from .components.contact import contact

def index() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                hero(),
                about(),
                services(),
                projects(),
                contact(),
                max_width="800px",
                width="100%",
                padding_x="2em",
                spacing="6",
            ),
        ),
        # Aplicamos el estilo base a toda la página
        style=BASE_STYLE,
        min_height="100vh",
    )

import os
from fastapi.staticfiles import StaticFiles

app = rx.App(
    style=BASE_STYLE,
)

app = rx.App(
    style=BASE_STYLE,
)

app.add_page(
    index, 
    title="Argos-Dev | Portafolio",
    description="Portafolio profesional de Argos-Dev. Programador de aplicaciones web y de escritorio."
)

# Si estamos en producción, preparamos la unión de backend y frontend
if os.getenv("REFLEX_ENV") == "prod":
    def mount_static():
        # Buscamos la carpeta de la web
        static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".web", "_static")
        if os.path.exists(static_dir):
            app._api.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
    
    # Le decimos a la app que ejecute esto en cuanto arranque
    app._api.add_event_handler("startup", mount_static)
