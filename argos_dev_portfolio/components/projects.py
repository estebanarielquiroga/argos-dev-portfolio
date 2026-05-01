import reflex as rx
from ..styles.styles import Color, heading_style, card_style

def project_card(title: str, description: str, image: str, tags: list) -> rx.Component:
    return rx.vstack(
        rx.image(
            src=image,
            width="100%",
            height="200px",
            object_fit="cover",
            border_radius="1em 1em 0 0",
        ),
        rx.vstack(
            rx.heading(title, size="5", style=heading_style),
            rx.text(description, size="2", color=Color.TEXT_MUTED),
            rx.hbox(
                *[rx.badge(tag, variant="outline", color_scheme="violet") for tag in tags],
                spacing="2",
                flex_wrap="wrap",
            ),
            padding="1.5em",
            spacing="3",
            align_items="start",
        ),
        style=card_style,
        overflow="hidden",
        height="100%",
    )

def projects() -> rx.Component:
    return rx.vstack(
        rx.heading("Proyectos Destacados", size="8", style=heading_style, padding_bottom="1em"),
        rx.grid(
            project_card(
                "TaskMaster Desktop",
                "Gestor de tareas avanzado con sincronización en la nube y dashboard de productividad.",
                "/project1.png",
                ["Python", "Reflex", "SQLite"]
            ),
            project_card(
                "Analytics Pro",
                "Plataforma web para visualización de datos complejos y reportes en tiempo real.",
                "/project2.png",
                ["FastAPI", "React", "PostgreSQL"]
            ),
            project_card(
                "StockFlow",
                "Sistema de control de inventario móvil para pequeños negocios y depósitos.",
                "/project3.png",
                ["Python", "Mobile-First", "API Rest"]
            ),
            columns=rx.breakpoints(initial="1", sm="2", lg="3"),
            spacing="6",
            width="100%",
        ),
        id="projects",
        spacing="5",
        align_items="center",
        padding_y="4em",
        width="100%",
    )
