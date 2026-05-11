import reflex as rx
from ..layout import layout
from ..styles.styles import Color, heading_style, card_style, button_style
from ..components.ads import ad_horizontal_banner

@rx.page(route="/blog", title="Recursos y Blog | Argos-Dev")
def blog_page() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Recursos de Autoridad", size="9", style=heading_style, color=Color.TEXT),
            rx.text(
                "Guías, tutoriales y artículos sobre la automatización administrativa, VBA, IA y desarrollo desktop.",
                color=Color.TEXT_MUTED,
                size="4",
                max_width="700px",
                text_align="center"
            ),
            
            # Ads Zone 1
            ad_horizontal_banner(),
            
            # Categorías
            rx.hstack(
                rx.badge("IA en la Oficina", color_scheme="violet", size="2"),
                rx.badge("VBA Avanzado", color_scheme="blue", size="2"),
                rx.badge("Gestión de Procesos", color_scheme="green", size="2"),
                rx.badge("Desarrollo Desktop", color_scheme="orange", size="2"),
                spacing="4",
                flex_wrap="wrap",
                margin_bottom="2em"
            ),
            
            # Artículos Recientes (Grid)
            rx.grid(
                rx.box(
                    rx.vstack(
                        rx.box(
                            width="100%", height="150px", background_color=Color.SECONDARY_BG, border_radius="0.5em",
                            border=f"1px solid {Color.GLASS_BORDER}"
                        ), # Placeholder Imagen
                        rx.badge("VBA Avanzado", color_scheme="blue", size="1", variant="outline"),
                        rx.heading("Cómo automatizar reportes de Excel en 5 minutos", size="5", style=heading_style),
                        rx.text("Aprende a usar macros para consolidar datos de múltiples archivos automáticamente...", color=Color.TEXT_MUTED, size="2"),
                        rx.link(rx.text("Leer más ->", color=Color.ACCENT, font_weight="600", font_size="0.9em"), href="#"),
                        spacing="3",
                        align_items="start",
                    ),
                    style=card_style,
                ),
                rx.box(
                    rx.vstack(
                        rx.box(
                            width="100%", height="150px", background_color=Color.SECONDARY_BG, border_radius="0.5em",
                            border=f"1px solid {Color.GLASS_BORDER}"
                        ), # Placeholder Imagen
                        rx.badge("Desarrollo Desktop", color_scheme="orange", size="1", variant="outline"),
                        rx.heading("Python y Tkinter: Construyendo interfaces locales B2B", size="5", style=heading_style),
                        rx.text("Por qué el desarrollo local sigue siendo clave para empresas con bases de datos on-premise...", color=Color.TEXT_MUTED, size="2"),
                        rx.link(rx.text("Leer más ->", color=Color.ACCENT, font_weight="600", font_size="0.9em"), href="#"),
                        spacing="3",
                        align_items="start",
                    ),
                    style=card_style,
                ),
                columns=rx.breakpoints(initial="1", md="2"),
                spacing="6",
                width="100%",
            ),
            
            spacing="6",
            align_items="center",
            width="100%",
        )
    )
