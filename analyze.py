
import reflex as rx
from AI_driven_code_reviewer.components.navbar import navbar
from AI_driven_code_reviewer.components.footer import footer
from AI_driven_code_reviewer.components.state import AnalyzeState

def analyze_page():
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("AI Code Reviewer", size="8"),
                
                # Input and Corrected Code side-by-side
                rx.grid(
                    rx.vstack(
                        rx.badge("Your Original Code", color_scheme="indigo"),
                        rx.text_area(
                            on_change=AnalyzeState.set_user_code, 
                            height="350px", width="100%",
                            style={"font-family": "monospace"}
                        ),
                    ),
                    rx.vstack(
                        rx.badge("Corrected Code", color_scheme="green"),
                        rx.text_area(
                            value=AnalyzeState.corrected_code, 
                            read_only=True, height="350px", width="100%",
                            style={"font-family": "monospace", "background_color": "#f8f9fa"}
                        ),
                    ),
                    columns="2", spacing="4", width="100%",
                ),
                
                rx.button(
                    "Analyze & Correct Code", 
                    on_click=AnalyzeState.process_code,
                    loading=AnalyzeState.is_loading,
                    width="100%", size="3"
                ),

                rx.divider(),

                # AI Suggestions and Feedback
                rx.vstack(
                    rx.heading("AI Suggestions & Feedback", size="5"),
                    rx.card(
                        rx.markdown(AnalyzeState.ai_suggestions), # Use markdown for better AI text formatting
                        width="100%",
                        padding="20px"
                    ),
                    
                    # Cleanup Report
                    rx.hstack(
                        rx.card(
                            rx.text("Variable Cleanup", font_weight="bold"),
                            rx.text(AnalyzeState.unused_vars),
                            width="100%", color_scheme="orange"
                        ),
                        rx.card(
                            rx.text("Import Cleanup", font_weight="bold"),
                            rx.text(AnalyzeState.unused_imports),
                            width="100%", color_scheme="red"
                        ),
                        width="100%", spacing="4"
                    ),
                    width="100%", align_items="start"
                ),
                spacing="6", padding_y="40px",
            ),
            size="4",
        ),
        footer(),
    )
    
"""
import reflex as rx
from AI_driven_code_reviewer.components.navbar import navbar
from AI_driven_code_reviewer.components.footer import footer
from AI_driven_code_reviewer.components.state import AnalyzeState
"""
"""
def analyze_page():
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("Code Analysis & AI Assistant", size="8"),
                
                # --- [Section 1: The Original Code Reviewer UI] ---
                # (Keep your existing grid with user_code and corrected_code here)
                
                rx.divider(margin_y="3em"),

                # --- [Section 2: The AI Assistant Chat] ---
                rx.vstack(
                    rx.heading("Ask the AI Assistant", size="5"),
                    rx.input(
                        placeholder="Ask anything about your code (e.g. 'How do I optimize this loop?')",
                        on_change=AnalyzeState.set_user_question,
                        width="100%",
                    ),
                    rx.button(
                        rx.cond(AnalyzeState.is_chatting, rx.spinner(), "Send Question"),
                        on_click=AnalyzeState.ask_assistant,
                        color_scheme="indigo",
                        width="100%"
                    ),
                    
                    # Display the AI's specific answer
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
    """
"""
import reflex as rx
from AI_driven_code_reviewer.components.navbar import navbar
from AI_driven_code_reviewer.components.footer import footer
from .state import AnalyzeState

def analyze_page():
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("AI Code Reviewer", size="8"),
                rx.grid(
                    rx.vstack(
                        rx.badge("Your Original Code", color_scheme="indigo"),
                        rx.text_area(
                            on_change=AnalyzeState.set_user_code, 
                            height="350px", width="100%",
                            style={"font-family": "monospace"}
                        ),
                    ),
                    rx.vstack(
                        rx.badge("Corrected Code", color_scheme="green"),
                        rx.text_area(
                            value=AnalyzeState.corrected_code, 
                            read_only=True, height="350px", width="100%",
                            style={"font-family": "monospace", "background_color": "#f8f9fa"}
                        ),
                    ),
                    columns="2", spacing="4", width="100%",
                ),
                rx.button(
                    "Analyze & Correct Code", 
                    on_click=AnalyzeState.process_code,
                    loading=AnalyzeState.is_loading,
                    width="100%", size="3"
                ),
                rx.divider(),
                rx.vstack(
                    rx.heading("AI Suggestions & Feedback", size="5"),
                    rx.card(
                        rx.markdown(AnalyzeState.ai_suggestions),
                        width="100%", padding="20px"
                    ),
                    rx.hstack(
                        rx.card(
                            rx.text("Variable Cleanup", font_weight="bold"),
                            rx.text(AnalyzeState.unused_vars),
                            width="100%", color_scheme="orange"
                        ),
                        rx.card(
                            rx.text("Import Cleanup", font_weight="bold"),
                            rx.text(AnalyzeState.unused_imports),
                            width="100%", color_scheme="red"
                        ),
                        width="100%", spacing="4"
                    ),
                    width="100%", align_items="start"
                ),
                spacing="6", padding_y="40px",
            ),
            size="4",
        ),
        footer(),
    )
    """