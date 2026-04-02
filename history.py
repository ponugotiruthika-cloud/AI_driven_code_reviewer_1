import reflex as rx
from .navbar import navbar
from .footer import footer
from .state import AnalyzeState

def history_page():
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("Analysis History", size="8"),
                rx.text("Review your past code optimizations."),
                
                rx.cond(
                    AnalyzeState.history.length() == 0,
                    rx.card(
                        rx.text("No history found. Start by analyzing some code!", color_scheme="gray"),
                        padding="2em", width="100%", text_align="center"
                    ),
                    rx.vstack(
                        rx.foreach(
                            AnalyzeState.history,
                            lambda item: rx.card(
                                rx.vstack(
                                    rx.hstack(
                                        rx.badge("Session", color_scheme="indigo"),
                                        rx.spacer(),
                                        rx.text(item["timestamp"], size="2", color_scheme="gray"),
                                    ),
                                    rx.text("Code Preview:", font_weight="bold"),
                                    rx.code(item["original"], width="100%"),
                                    rx.text("AI Summary:", font_weight="bold"),
                                    rx.markdown(item["suggestions"]),
                                    align_items="start",
                                    spacing="2",
                                ),
                                width="100%",
                                margin_bottom="1em",
                            )
                        ),
                        rx.button(
                            "Clear History", 
                            on_click=AnalyzeState.clear_history, 
                            color_scheme="red", variant="soft"
                        ),
                        width="100%",
                    )
                ),
                spacing="6", padding_y="40px",
            ),
            size="4",
        ),
        footer(),
    )