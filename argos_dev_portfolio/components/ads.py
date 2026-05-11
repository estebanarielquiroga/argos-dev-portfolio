import reflex as rx
from ..styles.styles import Color

def ad_placeholder(text: str = "Espacio Publicitario", height: str = "90px", width: str = "100%", max_width: str = "728px") -> rx.Component:
    """Un componente reutilizable para marcar las zonas donde irán los bloques de Google Ads."""
    return rx.box(
        rx.center(
            rx.text(text, color=Color.TEXT_MUTED, font_size="0.8em"),
            width="100%",
            height=height,
            background_color=Color.SECONDARY_BG,
            border=f"1px dashed {Color.GLASS_BORDER}",
        ),
        width=width,
        max_width=max_width,
        margin_y="2em",
        padding="0.5em",
        background_color="rgba(255, 255, 255, 0.02)",
        border_radius="0.5em"
    )

def ad_in_article() -> rx.Component:
    """Anuncio específico para intercalar en artículos del blog (Native/In-article)."""
    return ad_placeholder(text="Google Ads: In-Article", height="250px")

def ad_horizontal_banner() -> rx.Component:
    """Anuncio clásico horizontal (Leaderboard)."""
    return ad_placeholder(text="Google Ads: Horizontal Banner (728x90)", height="90px")

def ad_responsive_square() -> rx.Component:
    """Anuncio adaptable para móviles o barras laterales."""
    return ad_placeholder(text="Google Ads: Responsive Square", height="250px", max_width="300px")
