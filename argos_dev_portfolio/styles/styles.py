import reflex as rx

# Colores (Tema Oscuro y Neón)
class Color:
    BACKGROUND = "#0F172A"  # Slate 900 (Fondo principal muy oscuro)
    SECONDARY_BG = "#1E293B" # Slate 800 (Fondo secundario para tarjetas)
    TEXT = "#F8FAFC"        # Slate 50 (Texto claro)
    TEXT_MUTED = "#94A3B8"  # Slate 400 (Texto secundario)
    ACCENT = "#38BDF8"      # Light Blue 400 (Acento principal tipo neón)
    ACCENT_HOVER = "#0284C7" # Light Blue 600

# Estilos Generales
BASE_STYLE = {
    "background_color": Color.BACKGROUND,
    "color": Color.TEXT,
    "font_family": "Inter, sans-serif",
    "::selection": {
        "background_color": Color.ACCENT,
        "color": Color.BACKGROUND,
    }
}

# Estilos específicos
button_style = {
    "background_color": Color.ACCENT,
    "color": Color.BACKGROUND,
    "font_weight": "bold",
    "padding": "1em 2em",
    "border_radius": "0.5em",
    "_hover": {
        "background_color": Color.ACCENT_HOVER,
        "cursor": "pointer"
    }
}

heading_style = {
    "color": Color.TEXT,
    "font_family": "Inter, sans-serif",
    "font_weight": "bold",
}

card_style = {
    "background_color": Color.SECONDARY_BG,
    "padding": "2em",
    "border_radius": "1em",
    "box_shadow": "0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)",
    "_hover": {
        "border": f"1px solid {Color.ACCENT}",
    }
}
