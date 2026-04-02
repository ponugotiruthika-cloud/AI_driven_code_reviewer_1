 
import reflex as rx
from .state import AnalyzeState

def footer():
    return rx.vstack(
        rx.divider(),
        # 1. Links Row (Centered)
        rx.hstack(
            rx.link("About", on_click=AnalyzeState.toggle_about, cursor="pointer", weight="medium"),
            rx.link("GitHub", href="https://github.com/yourusername/your-repo", is_external=True, weight="medium"),
            rx.link("Contact", on_click=AnalyzeState.toggle_contact, cursor="pointer", weight="medium"),
            spacing="6",
            justify="center",
            width="100%",
            margin_top="1em",
        ),
        # 2. Copyright Row (Underneath the links)
        rx.text(
            "© 2026 AI Code Reviewer", 
            color_scheme="gray", 
            size="2",
            margin_top="0.5em"
        ),

        # --- ABOUT MODAL ---
        rx.dialog.root(
            rx.dialog.content(
                rx.dialog.title("About AI Code Reviewer"),
                rx.dialog.description(
                    "This tool uses advanced AI to analyze Python code, detect unused variables, "
                    "clean up imports, and provide logic optimizations in real-time."
                ),
                rx.button("Close", on_click=AnalyzeState.toggle_about, margin_top="1em"),
            ),
            open=AnalyzeState.show_about,
        ),

        # --- CONTACT MODAL ---
        rx.dialog.root(
            rx.dialog.content(
                rx.dialog.title("Contact Us"),
                rx.dialog.description(
                    "Have questions or feedback? Reach out at: support@aicuereviewer.com"
                ),
                rx.button("Close", on_click=AnalyzeState.toggle_contact, margin_top="1em"),
            ),
            open=AnalyzeState.show_contact,
        ),
        
        padding_y="2em",
        width="100%",
        align="center", # This centers everything inside the main vstack
    )
