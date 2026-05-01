import reflex as rx
from .styles.styles import BASE_STYLE
from .components.hero import hero
from .components.about import about
from .components.services import services
from .components.projects import projects
from .components.contact import contact
from .components.success_stories import success_stories
from .components.diagnosis import diagnosis_cta

# ============================================================
# Página principal del portafolio
# ============================================================
def index() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                hero(),
                about(),
                services(),
                success_stories(),
                diagnosis_cta(),
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

# ============================================================
# Configuración de la aplicación
# ============================================================
app = rx.App(
    style=BASE_STYLE,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Outfit:wght@100;300;400;500;600;700;800;900&display=swap",
    ],
)
app.add_page(
    index,
    title="Argos-Dev | Portafolio Premium",
    description="Explora el trabajo de Argos-Dev, desarrollador full-stack especializado en soluciones modernas y eficientes."
)
