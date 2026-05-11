import reflex as rx
from .components.navbar import navbar
from .components.footer import footer
from .styles.styles import BASE_STYLE

def layout(*children, **kwargs) -> rx.Component:
    """Un layout base que envuelve el contenido de las páginas con la navbar y el footer."""
    return rx.box(
        navbar(),
        rx.box(
            *children,
            width="100%",
            max_width="1200px",
            margin_x="auto",
            padding_x=["1em", "2em", "2em", "2em"],
            padding_y="4em",
            **kwargs,
        ),
        footer(),
        style=BASE_STYLE,
        min_height="100vh",
        display="flex",
        flex_direction="column",
    )
