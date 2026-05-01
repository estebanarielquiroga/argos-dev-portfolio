import reflex as rx
from ..styles.styles import Color, heading_style, button_style

def diagnosis_cta() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.badge("OFERTA ESPECIAL", color_scheme="violet", variant="soft", border_radius="full", padding_x="1em"),
                rx.heading("Diagnóstico Gratuito de 15 Minutos", size="8", style=heading_style, text_align="center"),
                rx.text(
                    "Identifiquemos juntos los cuellos de botella en tus procesos. Agendá una sesión rápida y sin compromiso para descubrir cómo la automatización y la IA pueden impulsar tu negocio.",
                    size="4",
                    color=Color.TEXT_MUTED,
                    text_align="center",
                    max_width="600px",
                ),
                rx.link(
                    rx.button(
                        rx.hstack(
                            rx.icon(tag="calendar", size=20),
                            rx.text("Agendar Sesión Ahora"),
                            gap="3",
                            align_items="center",
                        ),
                        style=button_style,
                        size="4",
                    ),
                    href="https://wa.me/3875021777?text=Hola,%20me%20interesa%20agendar%20el%20diagnóstico%20gratuito%20de%2015%20minutos.",
                    is_external=True,
                ),
                gap="5",
                align_items="center",
                padding="3em",
                background=f"linear-gradient(135deg, {Color.ACCENT}22, transparent)",
                border=f"1px solid {Color.ACCENT}44",
                border_radius="1.5em",
                width="100%",
                box_shadow=f"0 0 20px {Color.ACCENT}11",
            ),
        ),
        padding_y="4em",
        width="100%",
    )
