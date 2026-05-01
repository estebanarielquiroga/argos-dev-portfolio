import reflex as rx
from ..styles.styles import Color, heading_style, card_style

def service_card(title: str, description: str, icon: str) -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.icon(tag=icon, size=30, color=Color.ACCENT),
            padding="1em",
            background=f"{Color.ACCENT}11",
            border_radius="1em",
        ),
        rx.heading(title, size="5", style=heading_style),
        rx.text(description, size="2", color=Color.TEXT_MUTED, text_align="center"),
        style=card_style,
        align_items="center",
        spacing="4",
        width="100%",
    )

def services() -> rx.Component:
    return rx.vstack(
        rx.heading("Servicios Especializados", size="8", style=heading_style, padding_bottom="1em"),
        rx.grid(
            service_card(
                "Desarrollo Desktop",
                "Software robusto a medida diseñado para optimizar procesos internos y tareas críticas.",
                "monitor",
            ),
            service_card(
                "Desarrollo Web",
                "Experiencias digitales modernas, rápidas y optimizadas para cualquier dispositivo.",
                "globe",
            ),
            service_card(
                "Automatización",
                "Scripts y herramientas inteligentes para eliminar tareas repetitivas y errores humanos.",
                "zap",
            ),
            columns=rx.breakpoints(initial="1", sm="2", lg="3"),
            spacing="6",
            width="100%",
        ),
        spacing="5",
        align_items="center",
        padding_y="4em",
        width="100%",
    )
