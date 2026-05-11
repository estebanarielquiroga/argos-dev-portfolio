import reflex as rx
from ..layout import layout
from ..styles.styles import Color, heading_style, card_style, button_style

@rx.page(route="/soluciones/gestion-sanciones/descarga-exitosa-xyz987", title="Descarga de Sistema | Argos-Dev")
def sanciones_success() -> rx.Component:
    return layout(
        rx.vstack(
            rx.icon("check-circle", size=80, color=Color.ACCENT, margin_bottom="1em"),
            rx.heading("¡Gracias por tu compra!", size="9", style=heading_style, color=Color.TEXT, text_align="center"),
            rx.text(
                "Tu pago ha sido procesado exitosamente. Ya puedes descargar tu Sistema de Gestión de Sanciones.",
                color=Color.TEXT_MUTED,
                size="5",
                max_width="600px",
                text_align="center",
            ),
            
            rx.box(
                rx.vstack(
                    rx.icon("download", size=48, color=Color.ACCENT),
                    rx.heading("Archivo Listo", size="6", style=heading_style),
                    rx.text("sanciones.accdr (Access Runtime)", color=Color.TEXT_MUTED, size="3"),
                    rx.button(
                        "Descargar Archivo Ahora", 
                        on_click=rx.download(url="/sanciones.accdr"),
                        style=button_style, 
                        width="100%", 
                        size="4",
                        margin_top="1em"
                    ),
                    spacing="4",
                    align_items="center",
                    width="100%"
                ),
                style=card_style,
                width="100%",
                max_width="500px",
                margin_y="3em"
            ),
            
            rx.text(
                "Por favor, guarda el archivo en un lugar seguro. Si tienes problemas con la descarga, contáctanos.",
                color=Color.TEXT_MUTED,
                size="2",
                text_align="center"
            ),
            
            spacing="6",
            width="100%",
            align_items="center",
            padding_y="4em"
        )
    )
