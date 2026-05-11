import reflex as rx
from .styles.styles import BASE_STYLE
from .layout import layout
from .components.hero import hero
from .components.about import about
from .components.services import services
from .components.projects import projects
from .components.contact import contact
from .components.success_stories import success_stories
from .components.diagnosis import diagnosis_cta
from .components.ads import ad_horizontal_banner

# Importar las páginas para que Reflex las registre
from . import pages

# ============================================================
# Página principal del portafolio (Inicio)
# ============================================================
@rx.page(route="/", title="Argos-Dev | Soluciones B2B y Automatización")
def index() -> rx.Component:
    return layout(
        rx.vstack(
            hero(),
            # Ads Zone 0
            rx.center(ad_horizontal_banner(), width="100%"),
            about(),
            services(),
            success_stories(),
            diagnosis_cta(),
            projects(),
            contact(),
            spacing="8",
            width="100%",
        )
    )

# ============================================================
# Configuración de la aplicación
# ============================================================
app = rx.App(
    style=BASE_STYLE,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Outfit:wght@100;300;400;500;600;700;800;900&display=swap",
    ],
    head_components=[
        rx.script(
            src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5966960176374095",
            async_=True,
            crossorigin="anonymous",
        ),
    ],
)
