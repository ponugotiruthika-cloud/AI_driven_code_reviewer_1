 
 
import reflex as rx
from .components.navbar import navbar
from .components.footer import footer
from .components.analyze import analyze_page
from .components.assistant import assistant_page
from .components.history import history_page

def index() -> rx.Component:
    """The Home/Landing Page."""
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("AI-Driven Code Reviewer", size="9", margin_top="2em"),
                rx.text(
                    "Optimize your logic, clean up unused code, and chat with an AI assistant.",
                    size="5",
                    color_scheme="gray",
                ),
                rx.hstack(
                    rx.link(
                        rx.button(
                            "Get Started", 
                            size="4", 
                            color_scheme="indigo", 
                            variant="solid"
                        ),
                        href="/analyze",
                    ),
                    rx.link(
                        rx.button(
                            "Talk to Assistant", 
                            size="4", 
                            color_scheme="gray", 
                            variant="outline"
                        ),
                        href="/assistant",
                    ),
                    spacing="4",
                    margin_top="2em",
                ),
                align_items="center",
                text_align="center",
                spacing="5",
            ),
            size="4",
        ),
        footer(),
        background="radial-gradient(circle at top center, var(--indigo-2), transparent)",
        min_height="100vh",
    )

# 1. Initialize the App
app = rx.App(
    theme=rx.theme(
        appearance="light", 
        has_background=True, 
        accent_color="indigo"
    ),
)

# 2. Add the Pages and Routes
# This connects the "Get Started" button logic
app.add_page(index, route="/")

# This is the Page with 2 Text Areas (Original vs Corrected)
app.add_page(analyze_page, route="/analyze")

# This is the Page for the AI Assistant Chat
app.add_page(assistant_page, route="/assistant")
app.add_page(history_page, route="/history")
