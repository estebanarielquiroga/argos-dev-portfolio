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

# Si estamos en producción, hacemos que el backend sirva los archivos de la web
if os.getenv("REFLEX_ENV") == "prod":
    @app.api.on_event("startup")
    def mount_static():
        # Buscamos la carpeta donde Reflex exporta la web
        static_dir = os.path.join(os.getcwd(), ".web", "_static")
        if os.path.exists(static_dir):
            app.api.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

app.add_page(
    index, 
    title="Argos-Dev | Portafolio",
    description="Portafolio profesional de Argos-Dev. Programador de aplicaciones web y de escritorio."
)
