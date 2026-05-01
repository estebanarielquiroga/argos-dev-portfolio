import reflex as rx
from ..styles.styles import Color, heading_style, button_style

def contact() -> rx.Component:
    whatsapp_msg = "Hola Argos-Dev, me gustaría contactarte por tus servicios."
    whatsapp_url = f"https://wa.me/3875021777?text={whatsapp_msg.replace(' ', '%20')}"
    # Usamos el enlace de composición de Gmail para que funcione en cualquier sistema
    # sin necesidad de tener un cliente de correo instalado.
    email_url = "https://mail.google.com/mail/?view=cm&to=quirodev.ea@gmail.com&su=Consulta desde Argos-Dev&body=Hola, me gustaría contactarte por tus servicios."

    return rx.vstack(
        rx.heading("Iniciemos un Proyecto", size="8", style=heading_style),
        rx.text(
            "¿Tenés una idea o necesidad en mente? Estoy listo para ayudarte a hacerla realidad.",
            size="4",
            color=Color.TEXT_MUTED,
            text_align="center",
            max_width="500px",
        ),
        rx.flex(
            rx.link(
                rx.button(
                    rx.hstack(
                        rx.icon(tag="mail", size=20),
                        rx.text("Enviar Correo"),
                        gap="3",
                        align_items="center",
                    ),
                    style=button_style,
                ),
                href=email_url,
                is_external=True,
            ),
            rx.link(
                rx.button(
                    rx.hstack(
                        rx.icon(tag="message-circle", size=20),
                        rx.text("Chatear por WhatsApp"),
                        gap="3",
                        align_items="center",
                    ),
                    style=button_style,
                    background_color="#10b981", # Emerald 500
                    _hover={"background_color": "#059669", "transform": "translateY(-2px)"},
                ),
                href=whatsapp_url,
                is_external=True,
            ),
            gap="5",
            direction=rx.breakpoints(initial="column", sm="row"),
            justify="center",
            padding_top="3em",
        ),
        spacing="5",
        align_items="center",
        padding_y="6em",
        width="100%",
    )
