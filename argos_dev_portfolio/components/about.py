import reflex as rx
from ..styles.styles import Color, heading_style

def about() -> rx.Component:
    return rx.vstack(
        rx.heading("Sobre Mí", size="7", style=heading_style),
        rx.text(
            "Proactivo y resolutivo, con experiencia en el ámbito de la seguridad y conocimientos sólidos en informática.",
            size="4",
            color=Color.TEXT_MUTED,
            text_align="center",
            max_width="600px",
        ),
        spacing="4",
        align_items="center",
        padding_y="2em",
        width="100%",
    )
