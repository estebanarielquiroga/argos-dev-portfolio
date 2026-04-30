import reflex as rx
from ..styles.styles import Color, heading_style, card_style

def projects() -> rx.Component:
    return rx.vstack(
        rx.heading("Proyectos", size="7", style=heading_style),
        rx.box(
            rx.vstack(
                rx.icon(tag="construction", size=50, color=Color.ACCENT),
                rx.heading("Próximamente", size="5", color=Color.TEXT),
                rx.text(
                    "Estoy trabajando en aplicaciones increíbles. Pronto podrás ver mis proyectos aquí.",
                    color=Color.TEXT_MUTED,
                    text_align="center"
                ),
                align_items="center",
                spacing="4",
            ),
            style=card_style,
            width="100%",
            max_width="600px",
            padding="3em",
        ),
        spacing="5",
        align_items="center",
        padding_y="4em",
        width="100%",
    )
