import reflex as rx
from ..layout import layout
from ..styles.styles import Color, heading_style, card_style, button_style
from ..components.ads import ad_horizontal_banner, ad_responsive_square

@rx.page(route="/soluciones/gestion-rrhh", title="Gestor de Recursos Humanos | Argos-Dev")
def rrhh_landing() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Gestor de Base de Datos de Recursos Humanos", size="9", style=heading_style, color=Color.TEXT, text_align="center"),
            rx.text(
                "Solución integral para administrar el personal, controlar licencias y generar reportes de asistencia.",
                color=Color.TEXT_MUTED,
                size="5",
                max_width="800px",
                text_align="center",
            ),
            
            # Ads Zone 0
            ad_horizontal_banner(),
            
            rx.grid(
                rx.vstack(
                    rx.heading("Características del Sistema", size="6", style=heading_style),
                    rx.list.unordered(
                        rx.list.item("Base de datos centralizada del personal."),
                        rx.list.item("Cálculo y seguimiento de licencias."),
                        rx.list.item("Generación de estadísticas e informes en Excel."),
                        rx.list.item("Interfaz de usuario amigable y ejecutable independiente."),
                        color=Color.TEXT_MUTED,
                        spacing="3"
                    ),
                    
                    rx.heading("Beneficios", size="6", style=heading_style, margin_top="1em"),
                    rx.text("Ahorra tiempo, evita errores manuales y toma decisiones basadas en datos actualizados de tu equipo de trabajo.", color=Color.TEXT_MUTED),
                    
                    spacing="5",
                    align_items="start"
                ),
                
                rx.vstack(
                    rx.box(
                        rx.vstack(
                            rx.icon("users", size=48, color=Color.ACCENT),
                            rx.heading("Descargar Sistema", size="5", style=heading_style),
                            rx.text("Versión 64-bit | .exe | Portable", color=Color.TEXT_MUTED, size="2"),
                            rx.button(
                                "Descargar RRHH.exe", 
                                on_click=rx.download(url="/RRHH.exe"),
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
                    rx.heading("¿Tu nómina es muy compleja para una plantilla?", size="6", style=heading_style),
                    rx.text("Ofrecemos desarrollo de macros a medida e integraciones con sistemas contables existentes.", color=Color.TEXT_MUTED),
                    rx.link(rx.button("Solicitar Diagnóstico", style=button_style), href="/contacto"),
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
