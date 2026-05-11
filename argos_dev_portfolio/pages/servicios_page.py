import reflex as rx
from ..layout import layout
from ..styles.styles import Color, heading_style, card_style, button_style

@rx.page(route="/servicios", title="Servicios Profesionales | Argos-Dev")
def servicios_page() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Servicios de Transformación Digital B2B", size="9", style=heading_style, color=Color.TEXT, text_align="center"),
            rx.text(
                "Ayudamos a empresas a escalar sus operaciones mediante automatización, integraciones y software a medida.",
                color=Color.TEXT_MUTED,
                size="4",
                max_width="700px",
                text_align="center",
                margin_bottom="2em"
            ),
            
            rx.grid(
                rx.box(
                    rx.vstack(
                        rx.icon("briefcase", size=40, color=Color.ACCENT),
                        rx.heading("Consultoría en Automatización", size="6", style=heading_style),
                        rx.text("Evaluamos tus flujos de trabajo actuales e identificamos cuellos de botella que pueden ser automatizados con IA o VBA.", color=Color.TEXT_MUTED, size="3"),
                        spacing="4",
                        align_items="start",
                    ),
                    style=card_style,
                ),
                rx.box(
                    rx.vstack(
                        rx.icon("code", size=40, color=Color.ACCENT),
                        rx.heading("Desarrollo a Medida", size="6", style=heading_style),
                        rx.text("Creamos aplicaciones web y de escritorio (Python, Tkinter, MySQL) totalmente adaptadas a las necesidades de tu organización.", color=Color.TEXT_MUTED, size="3"),
                        spacing="4",
                        align_items="start",
                    ),
                    style=card_style,
                ),
                rx.box(
                    rx.vstack(
                        rx.icon("search", size=40, color=Color.ACCENT),
                        rx.heading("Auditoría Técnica", size="6", style=heading_style),
                        rx.text("Revisamos y optimizamos tus sistemas y bases de datos actuales para asegurar eficiencia, escalabilidad y seguridad.", color=Color.TEXT_MUTED, size="3"),
                        spacing="4",
                        align_items="start",
                    ),
                    style=card_style,
                ),
                columns=rx.breakpoints(initial="1", md="3"),
                spacing="6",
                width="100%",
            ),
            
            rx.divider(border_color=Color.GLASS_BORDER, margin_y="3em"),
            
            rx.box(
                rx.vstack(
                    rx.heading("¿Listo para optimizar tu empresa?", size="7", style=heading_style),
                    rx.link(rx.button("Agendar Diagnóstico Gratuito", style=button_style, size="4"), href="/contacto"),
                    align_items="center",
                    spacing="6",
                ),
                width="100%",
                padding_y="2em"
            ),
            
            spacing="6",
            align_items="center",
            width="100%",
        )
    )
