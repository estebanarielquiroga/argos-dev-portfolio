import reflex as rx

# ============================================================
# SISTEMA DE DISEÑO PREMIUM
# ============================================================

class Color:
    BACKGROUND = "#030712"    # Darker Slate/Grey
    SECONDARY_BG = "#111827"  # Gray 900
    TEXT = "#F9FAFB"         # White
    TEXT_MUTED = "#9CA3AF"   # Gray 400
    ACCENT = "#8B5CF6"       # Violet 500 (Vibrant)
    ACCENT_LIGHT = "#A78BFA" # Violet 400
    ACCENT_DARK = "#6D28D9"  # Violet 700
    GLASS_BG = "rgba(17, 24, 39, 0.7)"
    GLASS_BORDER = "rgba(255, 255, 255, 0.1)"

# Estilos de Glassmorphism
glass_style = {
    "background_color": Color.GLASS_BG,
    "backdrop_filter": "blur(12px)",
    "border": f"1px solid {Color.GLASS_BORDER}",
    "border_radius": "1.5em",
}

# Estilos Generales de la App
BASE_STYLE = {
    "background_color": Color.BACKGROUND,
    "color": Color.TEXT,
    "font_family": "'Outfit', sans-serif",
    "scroll_behavior": "smooth",
    "::selection": {
        "background_color": Color.ACCENT,
        "color": Color.TEXT,
    }
}

# Estilos de Componentes
button_style = {
    "background_color": Color.ACCENT,
    "color": Color.TEXT,
    "font_weight": "600",
    "padding": "0.75em 2em",
    "border_radius": "100px",
    "transition": "all 0.3s ease",
    "_hover": {
        "background_color": Color.ACCENT_DARK,
        "transform": "translateY(-2px)",
        "box_shadow": f"0 10px 20px -5px {Color.ACCENT_DARK}",
    }
}

heading_style = {
    "font_family": "'Outfit', sans-serif",
    "font_weight": "800",
    "letter_spacing": "-0.02em",
}

card_style = {
    **glass_style,
    "padding": "2em",
    "transition": "all 0.3s ease",
    "_hover": {
        "transform": "translateY(-5px)",
        "border": f"1px solid {Color.ACCENT}",
        "box_shadow": f"0 20px 40px -15px rgba(139, 92, 246, 0.3)",
    }
}
