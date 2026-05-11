import reflex as rx
from ..styles.styles import Color, glass_style, button_style

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Logo / Brand
            rx.link(
                rx.hstack(
                    rx.icon("hexagon", color=Color.ACCENT, size=30),
                    rx.text(
                        "Argos",
                        rx.text("Dev", color=Color.ACCENT, as_="span"),
                        font_size="1.5em",
                        font_weight="800",
                        letter_spacing="-0.02em"
                    ),
                    align_items="center",
                    spacing="2",
                ),
                href="/",
                _hover={"text_decoration": "none"}
            ),

            rx.spacer(),

            # Menú de Navegación (Desktop)
            rx.hstack(
                rx.link("Inicio", href="/", color=Color.TEXT_MUTED, _hover={"color": Color.TEXT}, font_weight="500"),
                
                # Mega-Menú Soluciones (Simplificado con un link por ahora)
                rx.menu.root(
                    rx.menu.trigger(
                        rx.button(
                            "Soluciones Gratis",
                            rx.icon("chevron-down", size=16),
                            variant="ghost",
                            color=Color.TEXT_MUTED,
                            _hover={"color": Color.TEXT},
                            font_weight="500",
                            size="2",
                        )
                    ),
                    rx.menu.content(
                        rx.menu.item("Macros Excel", on_click=rx.redirect("/soluciones/macros")),
                        rx.menu.item("Dashboards", on_click=rx.redirect("/soluciones/dashboards")),
                        rx.menu.item("Herramientas Gratuitas", on_click=rx.redirect("/soluciones")),
                        background_color=Color.SECONDARY_BG,
                        border=f"1px solid {Color.GLASS_BORDER}",
                        color=Color.TEXT,
                    ),
                ),
                
                rx.link("Servicios", href="/servicios", color=Color.TEXT_MUTED, _hover={"color": Color.TEXT}, font_weight="500"),
                rx.link("Blog", href="/blog", color=Color.TEXT_MUTED, _hover={"color": Color.TEXT}, font_weight="500"),
                rx.link("Sobre Mí", href="/sobre-mi", color=Color.TEXT_MUTED, _hover={"color": Color.TEXT}, font_weight="500"),
                spacing="6",
                display=["none", "none", "flex", "flex"], # Ocultar en móvil
                align_items="center",
            ),

            rx.spacer(),

            # Call to Action
            rx.link(
                rx.button(
                    "Diagnóstico Gratis",
                    style=button_style,
                ),
                href="/contacto",
                _hover={"text_decoration": "none"}
            ),
            
            width="100%",
            max_width="1200px",
            align_items="center",
            padding_y="1em",
            padding_x=["1em", "2em", "2em", "2em"],
        ),
        position="sticky",
        top="0",
        z_index="100",
        width="100%",
        display="flex",
        justify_content="center",
        **glass_style,
        border_top="none",
        border_left="none",
        border_right="none",
    )
