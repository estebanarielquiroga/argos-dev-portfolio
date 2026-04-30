import reflex as rx
from ..styles.styles import Color

def hero() -> rx.Component:
    return rx.vstack(
        rx.heading("ARGOS-DEV", size="9", color=Color.ACCENT),
        rx.text(
            "Soy un programador junior entusiasta y muy activo, enfocado en dar soluciones a problemas diarios que todos tenemos en lo personal y lo laboral.",
            size="5",
            color=Color.TEXT_MUTED,
            text_align="center",
            max_width="600px",
        ),
        spacing="5",
        align_items="center",
        padding_y="4em",
    )
