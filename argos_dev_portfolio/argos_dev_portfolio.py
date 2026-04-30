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
        style=BASE_STYLE,
        min_height="100vh",
    )

app = rx.App(
    style=BASE_STYLE,
)
app.add_page(
    index, 
    title="Argos-Dev | Portafolio",
    description="Portafolio profesional de Argos-Dev. Programador de aplicaciones web y de escritorio."
)
