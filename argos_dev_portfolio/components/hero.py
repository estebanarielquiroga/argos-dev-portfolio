import reflex as rx
from ..styles.styles import Color

def hero() -> rx.Component:
    return rx.center(
        rx.vstack(
            # Efecto de resplandor de fondo
            rx.box(
                width="300px",
                height="300px",
                background=f"radial-gradient(circle, {Color.ACCENT}33 0%, transparent 70%)",
                position="absolute",
                z_index="-1",
                filter="blur(40px)",
            ),
            rx.badge("DISPONIBLE PARA PROYECTOS", color_scheme="violet", variant="soft", border_radius="full", padding_x="1em"),
            rx.heading(
                "ARGOS-DEV",
                size="9",
                style=heading_style,
                background=f"linear-gradient(to right, {Color.TEXT}, {Color.ACCENT})",
                background_clip="text",
                color="transparent",
            ),
            rx.text(
                "Transformando ideas en soluciones digitales de alto impacto.",
                size="6",
                font_weight="500",
                color=Color.TEXT,
                text_align="center",
            ),
            rx.text(
                "Programador Full-Stack enfocado en crear aplicaciones modernas, eficientes y con una experiencia de usuario excepcional.",
                size="4",
                color=Color.TEXT_MUTED,
                text_align="center",
                max_width="600px",
            ),
            rx.button(
                "Ver Proyectos",
                style=button_style,
                on_click=rx.scroll_to("projects"),
            ),
            spacing="6",
            align_items="center",
            padding_y="6em",
        ),
        width="100%",
    )
