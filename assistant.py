 
import reflex as rx
from AI_driven_code_reviewer.components.navbar import navbar
from AI_driven_code_reviewer.components.footer import footer
from AI_driven_code_reviewer.components.state import AnalyzeState

def assistant_page():
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("Code AI Assistant", size="8"),
                rx.text("Paste code above or in the reviewer for context."),
                
                rx.divider(margin_y="2em"),

                # Chat UI
                rx.vstack(
                    rx.heading("Ask a question about your logic:", size="4"),
                    rx.input(
                        placeholder="e.g., Explain why I need a try-except block here?",
                        on_change=AnalyzeState.set_user_question,
                        width="100%",
                    ),
                    rx.button(
                        rx.cond(AnalyzeState.is_chatting, rx.spinner(), "Ask Assistant"),
                        on_click=AnalyzeState.ask_assistant,
                        color_scheme="indigo",
                        width="100%"
                    ),
                    # The Answer Box
                    rx.cond(
                        AnalyzeState.chat_answer != "",
                        rx.card(
                            rx.markdown(AnalyzeState.chat_answer),
                            background_color=rx.color("indigo", 2),
                            width="100%",
                            padding="1.5em",
                        )
                    ),
                    width="100%",
                    spacing="4",
                    background=rx.color("gray", 2),
                    padding="2em",
                    border_radius="15px",
                ),
                padding_y="40px",
            ),
            size="4",
        ),
        footer(),
    )
