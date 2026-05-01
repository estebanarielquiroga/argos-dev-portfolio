import reflex as rx
from ..styles.styles import Color, heading_style, card_style

def about() -> rx.Component:
    return rx.vstack(
        rx.heading("Sobre Mí", size="8", style=heading_style),
        rx.box(
            rx.text(
                "Proactivo y resolutivo, con experiencia en el ámbito de la seguridad y conocimientos sólidos en informática. Me apasiona aprender nuevas tecnologías y aplicarlas para resolver problemas reales.",
                size="4",
                color=Color.TEXT,
                text_align="center",
            ),
            style=card_style,
            max_width="700px",
            padding="2.5em",
        ),
        spacing="6",
        align_items="center",
        padding_y="4em",
        width="100%",
    )
