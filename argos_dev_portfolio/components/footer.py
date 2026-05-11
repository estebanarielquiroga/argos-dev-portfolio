import reflex as rx
from ..styles.styles import Color

def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.divider(border_color=Color.GLASS_BORDER, margin_y="2em"),
            rx.hstack(
                rx.vstack(
                    rx.hstack(
                        rx.icon("hexagon", color=Color.ACCENT, size=24),
                        rx.text(
                            "Argos",
                            rx.text("Dev", color=Color.ACCENT, as_="span"),
                            font_size="1.2em",
                            font_weight="800",
                        ),
                        align_items="center",
                    ),
                    rx.text(
                        "Automatización Administrativa de Alto Impacto para Empresas B2B.",
                        color=Color.TEXT_MUTED,
                        font_size="0.9em",
                        max_width="300px",
                    ),
                    rx.text(
                        "Basado en Salta, Argentina - Soluciones Globales",
                        color=Color.ACCENT_LIGHT,
                        font_size="0.8em",
                        font_weight="600"
                    ),
                    spacing="4",
                    align_items="start",
                ),
                
                rx.spacer(),
                
                rx.vstack(
                    rx.text("Enlaces", font_weight="600", color=Color.TEXT),
                    rx.link("Soluciones Gratis", href="/soluciones", color=Color.TEXT_MUTED, _hover={"color": Color.ACCENT}, font_size="0.9em"),
                    rx.link("Servicios B2B", href="/servicios", color=Color.TEXT_MUTED, _hover={"color": Color.ACCENT}, font_size="0.9em"),
                    rx.link("Blog / Recursos", href="/blog", color=Color.TEXT_MUTED, _hover={"color": Color.ACCENT}, font_size="0.9em"),
                    align_items="start",
                ),
                
                rx.spacer(),
                
                rx.vstack(
                    rx.text("Legal", font_weight="600", color=Color.TEXT),
                    rx.link("Aviso Legal", href="#", color=Color.TEXT_MUTED, _hover={"color": Color.ACCENT}, font_size="0.9em"),
                    rx.link("Política de Privacidad", href="#", color=Color.TEXT_MUTED, _hover={"color": Color.ACCENT}, font_size="0.9em"),
                    rx.link("Contacto", href="/contacto", color=Color.TEXT_MUTED, _hover={"color": Color.ACCENT}, font_size="0.9em"),
                    align_items="start",
                ),
                
                width="100%",
                align_items="start",
                flex_direction=["column", "column", "row", "row"],
                spacing="8",
            ),
            
            rx.center(
                rx.text(
                    "© 2024 Argos Dev. Todos los derechos reservados.",
                    color=Color.TEXT_MUTED,
                    font_size="0.8em",
                    margin_top="3em",
                ),
                width="100%"
            ),
            
            width="100%",
            max_width="1200px",
            padding_x=["1em", "2em", "2em", "2em"],
            padding_bottom="2em",
        ),
        width="100%",
        display="flex",
        justify_content="center",
        background_color=Color.SECONDARY_BG,
    )
