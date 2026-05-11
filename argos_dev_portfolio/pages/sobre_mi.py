import reflex as rx
from ..layout import layout
from ..styles.styles import Color, heading_style, card_style

@rx.page(route="/sobre-mi", title="Sobre Mí | Argos-Dev")
def sobre_mi() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Mi Trayectoria Técnica", size="9", style=heading_style, color=Color.TEXT),
            
            rx.grid(
                rx.box(
                    # Aquí iría la foto real para E-E-A-T
                    rx.box(
                        width="100%", 
                        height="300px", 
                        background_color=Color.SECONDARY_BG, 
                        border_radius="1em",
                        border=f"1px solid {Color.GLASS_BORDER}",
                        display="flex",
                        align_items="center",
                        justify_content="center"
                    ),
                    rx.text("Rocío - Fundadora de Argos Dev", color=Color.TEXT_MUTED, font_style="italic", margin_top="1em", text_align="center"),
                ),
                rx.vstack(
                    rx.heading("Transformando datos en decisiones", size="7", style=heading_style),
                    rx.text(
                        "Con base en Salta, Argentina, me especializo en desarrollar herramientas de automatización "
                        "y análisis de datos que permiten a las empresas operar de forma más eficiente.",
                        color=Color.TEXT_MUTED,
                        size="4",
                    ),
                    rx.text(
                        "Experiencia en automatización con VBA, desarrollo de aplicaciones desktop con Python y Tkinter, "
                        "y administración de bases de datos MySQL.",
                        color=Color.TEXT_MUTED,
                        size="4",
                    ),
                    
                    rx.divider(border_color=Color.GLASS_BORDER, margin_y="1em"),
                    
                    rx.heading("Certificaciones y Tecnologías", size="5", style=heading_style),
                    rx.hstack(
                        rx.badge("Python", color_scheme="blue"),
                        rx.badge("Excel / VBA", color_scheme="green"),
                        rx.badge("MySQL", color_scheme="orange"),
                        rx.badge("Tkinter", color_scheme="violet"),
                        rx.badge("FastAPI", color_scheme="teal"),
                        spacing="2",
                        flex_wrap="wrap"
                    ),
                    spacing="4",
                    align_items="start",
                    justify_content="center",
                    height="100%"
                ),
                columns=rx.breakpoints(initial="1", md="2"),
                spacing="8",
                width="100%",
                padding_y="2em",
            ),
            
            spacing="6",
            width="100%",
        )
    )
