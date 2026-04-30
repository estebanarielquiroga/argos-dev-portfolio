import reflex as rx
from ..styles.styles import Color, heading_style, button_style

def contact() -> rx.Component:
    # URL para WhatsApp. Reemplaza los espacios con %20 para la URL.
    whatsapp_msg = "Hola Argos-Dev, me gustaría contactarte por tus servicios."
    whatsapp_url = f"https://wa.me/3875021777?text={whatsapp_msg.replace(' ', '%20')}"
    # Usamos el enlace de composición de Gmail para que funcione en cualquier sistema
    # sin necesidad de tener un cliente de correo instalado.
    email_url = "https://mail.google.com/mail/?view=cm&to=quirodev.ea@gmail.com&su=Consulta desde Argos-Dev&body=Hola, me gustaría contactarte por tus servicios."

    return rx.vstack(
        rx.heading("Contacto", size="7", style=heading_style),
        rx.text(
            "¿Tienes un proyecto en mente? ¡Hablemos!",
            size="4",
            color=Color.TEXT_MUTED,
            text_align="center",
        ),
        rx.flex(
            rx.link(
                rx.button(
                    rx.icon(tag="mail"),
                    "Enviar Email",
                    style=button_style,
                    color_scheme="blue",
                    variant="solid",
                ),
                href=email_url,
                is_external=True,
            ),
            rx.link(
                rx.button(
                    rx.icon(tag="message-circle"),
                    "WhatsApp",
                    style=button_style,
                    color_scheme="green",
                    variant="solid",
                    background_color="#25D366", # Color oficial de WhatsApp
                    _hover={"background_color": "#128C7E", "cursor": "pointer"},
                ),
                href=whatsapp_url,
                is_external=True,
            ),
            spacing="4",
            flex_direction=["column", "row"],
            justify="center",
            padding_top="2em",
        ),
        spacing="4",
        align_items="center",
        padding_y="4em",
        width="100%",
    )
