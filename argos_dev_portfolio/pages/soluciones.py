import reflex as rx
from ..layout import layout
from ..styles.styles import Color, heading_style, card_style, button_style

@rx.page(route="/soluciones", title="Soluciones Gratuitas | Argos-Dev")
def soluciones() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("App Store de Productividad", size="9", style=heading_style, color=Color.TEXT),
            rx.text(
                "Descarga nuestras herramientas gratuitas (Macros, Dashboards) y transforma tus procesos manuales hoy mismo.",
                color=Color.TEXT_MUTED,
                size="4",
                max_width="600px",
                text_align="center"
            ),
            
            # Grid de soluciones
            rx.grid(
                rx.box(
                    rx.vstack(
                        rx.icon("file-lock", size=40, color=Color.ACCENT),
                        rx.heading("Sistema de Sanciones", size="6", style=heading_style),
                        rx.text("Gestión administrativa completa de faltas y sanciones institucionales en formato ACCDR.", color=Color.TEXT_MUTED, size="3"),
                        rx.link(rx.button("Ver y Descargar", style=button_style, width="100%"), href="/soluciones/gestion-sanciones", width="100%"),
                        spacing="4",
                        align_items="start",
                    ),
                    style=card_style,
                ),
                rx.box(
                    rx.vstack(
                        rx.icon("bar-chart", size=40, color=Color.ACCENT),
                        rx.heading("Dashboard Asistencia", size="6", style=heading_style),
                        rx.text("Panel interactivo para visualizar el presentismo mensual y alertas tempranas.", color=Color.TEXT_MUTED, size="3"),
                        rx.link(rx.button("Ver y Descargar", style=button_style, width="100%"), href="#", width="100%"),
                        spacing="4",
                        align_items="start",
                    ),
                    style=card_style,
                ),
                columns=rx.breakpoints(initial="1", md="2", lg="3"),
                spacing="6",
                width="100%",
                padding_y="3em",
            ),
            
            # CTA para servicios personalizados
            rx.box(
                rx.vstack(
                    rx.heading("¿Necesitas algo más específico?", size="7", style=heading_style),
                    rx.text("Desarrollamos soluciones a medida para los desafíos de tu empresa.", color=Color.TEXT_MUTED),
                    rx.link(rx.button("Solicitar Consultoría", style=button_style), href="/servicios"),
                    align_items="center",
                    spacing="4",
                ),
                style=card_style,
                width="100%",
                background_color=Color.SECONDARY_BG,
                margin_top="3em"
            ),
            
            spacing="6",
            align_items="center",
            width="100%",
        )
    )
