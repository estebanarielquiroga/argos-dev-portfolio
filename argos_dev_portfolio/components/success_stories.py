import reflex as rx
from ..styles.styles import Color, heading_style, card_style

def success_card(title: str, description: str, metric_before: str, metric_after: str, icon: str) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(tag=icon, size=24, color=Color.ACCENT),
            rx.heading(title, size="5", style=heading_style),
            gap="3",
            align_items="center",
        ),
        rx.text(description, size="3", color=Color.TEXT_MUTED),
        rx.divider(background=f"{Color.TEXT}33"),
        rx.hstack(
            rx.vstack(
                rx.text("Antes", size="1", color=Color.TEXT_MUTED, text_transform="uppercase", font_weight="bold"),
                rx.text(metric_before, size="3", color="#ef4444", text_decoration="line-through"),
                align_items="start",
                gap="1",
            ),
            rx.icon(tag="arrow-right", color=Color.TEXT_MUTED),
            rx.vstack(
                rx.text("Después", size="1", color=Color.TEXT_MUTED, text_transform="uppercase", font_weight="bold"),
                rx.text(metric_after, size="3", color="#10b981", font_weight="bold"),
                align_items="start",
                gap="1",
            ),
            justify="between",
            align_items="center",
            width="100%",
        ),
        style=card_style,
        spacing="4",
        width="100%",
    )

def success_stories() -> rx.Component:
    return rx.vstack(
        rx.heading("Soluciones Reales", size="8", style=heading_style, padding_bottom="1em"),
        rx.grid(
            success_card(
                "Automatización Contable",
                "Migración de carga manual de reportes a un sistema automatizado.",
                "4 horas manuales",
                "5 minutos con VBA",
                "file-spreadsheet",
            ),
            success_card(
                "Gestión Centralizada",
                "Unificación de información dispersa en un único sistema seguro.",
                "Datos sueltos por doquier",
                "Base de Datos (Python + Tkinter)",
                "database",
            ),
            columns=rx.breakpoints(initial="1", md="2"),
            spacing="6",
            width="100%",
        ),
        gap="5",
        align_items="center",
        padding_y="4em",
        width="100%",
    )
