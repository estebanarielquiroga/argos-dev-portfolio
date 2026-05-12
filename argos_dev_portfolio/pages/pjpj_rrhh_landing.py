import reflex as rx
from ..layout import layout
from ..styles.styles import Color, heading_style, card_style, button_style
from ..components.ads import ad_horizontal_banner, ad_responsive_square

@rx.page(route="/soluciones/pjpj-rrhh", title="Gestor de Personal PJPJ | Argos-Dev")
def pjpj_rrhh_landing() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Gestor de Personal PJPJ", size="9", style=heading_style, color=Color.TEXT, text_align="center"),
            rx.text(
                "Software especializado para la administración técnica y operativa del personal del programa PJPJ.",
                color=Color.TEXT_MUTED,
                size="5",
                max_width="800px",
                text_align="center",
            ),
            
            # Ads Zone 0
            ad_horizontal_banner(),
            
            rx.grid(
                rx.vstack(
                    rx.heading("Funcionalidades Clave", size="6", style=heading_style),
                    rx.list.unordered(
                        rx.list.item("Gestión integral de expedientes de personal."),
                        rx.list.item("Control de asistencia y licencias específicas."),
                        rx.list.item("Generación de reportes operativos en tiempo real."),
                        rx.list.item("Ejecutable portable de alto rendimiento (64-bit)."),
                        color=Color.TEXT_MUTED,
                        spacing="3"
                    ),
                    
                    rx.heading("Optimización Operativa", size="6", style=heading_style, margin_top="1em"),
                    rx.text("Diseñado específicamente para las necesidades de gestión del PJPJ, eliminando la burocracia manual y centralizando la información.", color=Color.TEXT_MUTED),
                    
                    spacing="5",
                    align_items="start"
                ),
                
                rx.vstack(
                    rx.box(
                        rx.vstack(
                            rx.icon("user-cog", size=48, color=Color.ACCENT),
                            rx.heading("Descargar Gestor PJPJ", size="5", style=heading_style),
                            rx.text("Versión 64-bit | .exe | Portable", color=Color.TEXT_MUTED, size="2"),
                            rx.text("Última actualización: 12 de Mayo 2026", color=Color.ACCENT, size="1", weight="bold"),
                            rx.button(
                                "Descargar PJPJ_RRHH.exe", 
                                on_click=rx.download(url="/PJPJ_RRHH.exe"),
                                style=button_style, 
                                width="100%", 
                                margin_top="1em"
                            ),
                            spacing="3",
                            align_items="center",
                            width="100%"
                        ),
                        style=card_style,
                        width="100%"
                    ),
                    
                    # Ads Zone 2 (Sidebar/Download)
                    rx.center(ad_responsive_square(), width="100%"),
                    
                    spacing="6",
                    align_items="center"
                ),
                columns=rx.breakpoints(initial="1", md="2"),
                spacing="8",
                width="100%",
                padding_y="3em",
            ),
            
            rx.divider(border_color=Color.GLASS_BORDER, margin_y="2em"),
            
            rx.box(
                rx.vstack(
                    rx.heading("¿Requieres soporte o personalización?", size="6", style=heading_style),
                    rx.text("Adaptamos nuestras herramientas a los flujos de trabajo específicos de tu institución.", color=Color.TEXT_MUTED),
                    rx.link(rx.button("Contactar Soporte", style=button_style), href="/contacto"),
                    align_items="center",
                    spacing="4",
                ),
                width="100%",
                background_color=Color.SECONDARY_BG,
                padding="3em",
                border_radius="1em",
                border=f"1px solid {Color.GLASS_BORDER}",
                text_align="center"
            ),
            
            spacing="6",
            width="100%",
            align_items="center"
        )
    )
