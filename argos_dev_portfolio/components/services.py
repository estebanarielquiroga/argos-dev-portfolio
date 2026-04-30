import reflex as rx
from ..styles.styles import Color, heading_style, card_style

def service_card(title: str, description: str, icon: str) -> rx.Component:
    return rx.vstack(
        rx.icon(tag=icon, size=40, color=Color.ACCENT),
        rx.heading(title, size="5", style=heading_style),
        rx.text(description, size="3", color=Color.TEXT_MUTED, text_align="center"),
        style=card_style,
        align_items="center",
        spacing="3",
        width=["100%", "45%"], # Responsive width
    )

def services() -> rx.Component:
    return rx.vstack(
        rx.heading("Mis Servicios", size="7", style=heading_style),
        rx.flex(
            service_card(
                "Aplicaciones de Escritorio",
                "Software a medida que permite solucionar problemas particulares y agilizar el día a día en el ámbito personal o laboral.",
                "monitor",
            ),
            service_card(
                "Aplicaciones Web",
                "Páginas y plataformas web modernas y funcionales que permiten mostrar quiénes somos y conectar con los clientes.",
                "globe",
            ),
            spacing="5",
            flex_direction=["column", "row"], # Responsive flex
            justify="center",
            width="100%",
        ),
        spacing="5",
        align_items="center",
        padding_y="4em",
        width="100%",
    )
