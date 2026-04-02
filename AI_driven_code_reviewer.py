 
"""
import reflex as rx
from AI_driven_code_reviewer.components.navbar import navbar
from AI_driven_code_reviewer.components.hero import hero
from AI_driven_code_reviewer.components.footer import footer
from code_analyzer import analyze_code_pipeline   # ✅ import your pipeline


# Reflex State to hold code and results
class AnalyzeState(rx.State):
    code: str = ""       # pasted code
    unused: list[str] = []   # unused variables
    suggestions: str = ""    # AI suggestions

    def run_analysis(self):
        if self.code.strip():
            result = analyze_code_pipeline(self.code)

            # Split results into unused + suggestions
            try:
                lines = result.splitlines()
                self.unused = [line for line in lines if "Unused Variables" in line or "unused_variables" in line]
                self.suggestions = "\n".join(
                    line for line in lines if "AI Suggestions" in line or not line.startswith("Unused Variables")
                )
            except Exception:
                self.unused = []
                self.suggestions = result
        else:
            self.suggestions = "⚠️ Please paste some code first."
            self.unused = []


def index():
    return rx.container(
        navbar(),
        hero(),
        footer(),
    )


def analyze():
    return rx.container(
        rx.vstack(
            rx.heading("Paste Your Code Below", size="6"),
            rx.text_area(
                placeholder="Paste your code here...",
                width="100%",
                height="300px",
                resize="vertical",
                value=AnalyzeState.code,
                on_change=AnalyzeState.set_code,   # bind input to state
            ),
            rx.button(
                "Analyze Code",
                variant="solid",
                color_scheme="blue",
                size="3",
                on_click=AnalyzeState.run_analysis,  # run pipeline
            ),
            # Results Panel
            rx.box(
                rx.vstack(
                    rx.heading("Unused Variables and imports", size="5"),
                    rx.cond(
                        AnalyzeState.unused,
                        rx.unordered_list(
                            rx.foreach(
                                AnalyzeState.unused,
                                lambda item: rx.list_item(item)
                            )

                        ),
                        rx.text("✅ No unused variables and imports found.")
                    ),
                    rx.heading("AI Suggestions", size="5", margin_top="10px"),
                    rx.text(AnalyzeState.suggestions),
                    spacing="3",
                    align="start"
                ),
                padding="15px",
                border="1px solid #ccc",
                border_radius="8px",
                margin_top="15px",
                width="100%",
                background_color="#f9f9f9"
            ),
            spacing="4",
            align="center"
        ),
        padding="20px"
    )


def history():
    return rx.container(
        rx.heading("History", size="6"),
        rx.text("About history"),
        padding="20px"
    )


def about():
    return rx.container(
        rx.heading("About", size="6"),
        rx.text("About app....."),
        padding="20px"
    )


app = rx.App()
app.add_page(index)
app.add_page(analyze, route="/analyze")
app.add_page(history, route="/history")
app.add_page(about, route="/about")
"""
"""
import reflex as rx
from code_analyzer import analyze_code_pipeline
from ai_suggester import get_ai_suggestions

class AnalyzeState(rx.State):
    code: str = ""
    language: str = "Python"
    result: dict = {
        "language": "",
        "report": "",
        "unused_vars": "",
        "unused_imports": "",
        "suggestions": "",
        "original_code": "",
        "corrected_code": "",
        "error": "",
    }

    def run_analysis(self):
        if self.code.strip():
            analysis = analyze_code_pipeline(self.code)
            self.result = {
                "language": f"Language Selected: {self.language}",
                "report": analysis.get("report", ""),
                "unused_vars": analysis.get("unused_vars", ""),
                "unused_imports": analysis.get("unused_imports", ""),
                "suggestions": "AI Suggestions:\n" + str(analysis.get("suggestions", "")),
                "original_code": analysis.get("original_code", ""),
                "corrected_code": analysis.get("corrected_code", ""),
                "error": analysis.get("error", ""),
            }
        else:
            self.result = {k: "" for k in self.result}
            self.result["error"] = "⚠️ Please paste some code first."


class AssistantState(rx.State):
    query: str = ""
    response: str = ""
    corrected_code: str = ""

    def run_assistant(self):
        if self.query.strip():
            code = AnalyzeState.code
            combined_prompt = f"User query: {self.query}\n\nCode:\n{code}"
            suggestion = get_ai_suggestions(combined_prompt)
            self.response = suggestion
            self.corrected_code = suggestion
        else:
            self.response = "⚠️ Please enter a query first."


def app_layout():
    return rx.hstack(
        # Sidebar
        rx.box(
            rx.vstack(
                rx.heading("AI Driven Code Reviewer", size="7", weight="bold", margin_bottom="20px"),
                rx.divider(),
                rx.link("Code Editor", href="/"),
                rx.link("Analysis Report", href="/analyze"),
                rx.link("AI Assistant", href="/assistant"),
                spacing="3",
                align="start"
            ),
            width="250px",
            height="100vh",
            padding="20px",
            background_color="#1e1e2f",
            color="white"
        ),

        # Main Content
        rx.box(
            rx.vstack(
                rx.heading("Intelligent Code Analysis", size="6"),
                rx.text_area(
                    placeholder="Paste your Python code here...",
                    width="100%",
                    height="300px",
                    resize="vertical",
                    value=AnalyzeState.code,
                    on_change=AnalyzeState.set_code,
                ),
                rx.button(
                    "Analyze Code",
                    variant="solid",
                    color_scheme="blue",
                    size="3",
                    on_click=AnalyzeState.run_analysis,
                ),
                rx.box(
                    rx.vstack(
                        rx.text(AnalyzeState.result.get("language", ""), weight="bold"),
                        rx.text(AnalyzeState.result.get("report", "")),
                        rx.text(AnalyzeState.result.get("unused_vars", ""), weight="bold"),
                        rx.text(AnalyzeState.result.get("unused_imports", ""), weight="bold"),
                        rx.text(AnalyzeState.result.get("suggestions", "")),
                        rx.text(AnalyzeState.result.get("error", "")),

                        # Two text areas side by side
                        rx.hstack(
                            rx.box(
                                rx.text("Original Code", weight="bold"),
                                rx.text_area(
                                    value=AnalyzeState.result.get("original_code", ""),
                                    width="100%",
                                    height="300px",
                                    read_only=True,
                                ),
                                rx.button(
                                    "Download Original Code",
                                    on_click=lambda: rx.download(
                                        AnalyzeState.result.get("original_code", ""),
                                        filename="original_code.py"
                                    ),
                                    margin_top="10px",
                                    color_scheme="purple"
                                ),
                                flex="1",
                                padding="10px"
                            ),
                            rx.box(
                                rx.text("Corrected Code", weight="bold"),
                                rx.text_area(
                                    value=AnalyzeState.result.get("corrected_code", ""),
                                    width="100%",
                                    height="300px",
                                    read_only=True,
                                ),
                                rx.hstack(
                                    rx.button(
                                        "Copy Corrected Code",
                                        on_click=[
                                            lambda: rx.set_clipboard(AnalyzeState.result.get("corrected_code", "")),
                                            lambda: rx.toast("✅ Corrected code copied!", duration=2000)
                                        ],
                                        color_scheme="blue"
                                    ),
                                    rx.button(
                                        "Download Corrected Code",
                                        on_click=lambda: rx.download(
                                            AnalyzeState.result.get("corrected_code", ""),
                                            filename="corrected_code.py"
                                        ),
                                        color_scheme="purple"
                                    ),
                                    spacing="3",
                                    margin_top="10px"
                                ),
                                flex="1",
                                padding="10px"
                            ),
                            spacing="4",
                        ),
                        spacing="2",
                        align="start"
                    ),
                    padding="15px",
                    border="1px solid #444",
                    border_radius="8px",
                    margin_top="15px",
                    width="100%",
                    background_color="#2a2a3d",
                    color="white"
                ),
                spacing="4",
                align="start"
            ),
            flex="1",
            padding="30px",
            background_color="#12121c",
            color="white"
        )
    )


def assistant_layout():
    return rx.box(
        rx.vstack(
            rx.heading("AI Assistant", size="6"),
            rx.text_area(
                placeholder="Enter your query here...",
                width="100%",
                height="150px",
                resize="vertical",
                value=AssistantState.query,
                on_change=AssistantState.set_query,
            ),
            rx.button(
                "Get Suggestions",
                variant="solid",
                color_scheme="green",
                size="3",
                on_click=AssistantState.run_assistant,
            ),
            rx.text(AssistantState.response),
            rx.box(
                rx.text("Corrected Code (AI Logic)", weight="bold"),
                rx.text_area(
                    value=AssistantState.corrected_code,
                    width="100%",
                    height="300px",
                    read_only=True,
                ),
                rx.hstack(
                    rx.button(
                        "Copy AI Corrected Code",
                        on_click=[
                            lambda: rx.set_clipboard(AssistantState.corrected_code),
                            lambda: rx.toast("✅ AI corrected code copied!", duration=2000)
                        ],
                        color_scheme="green"
                    ),
                    rx.button(
                        "Download AI Corrected Code",
                        on_click=lambda: rx.download(
                            AssistantState.corrected_code,
                            filename="ai_corrected_code.py"
                        ),
                        color_scheme="purple"
                    ),
                    spacing="3",
                    margin_top="10px"
                ),
                margin_top="15px"
            ),
            spacing="4",
            align="start"
        ),
        flex="1",
        padding="30px",
        background_color="#12121c",
        color="white"
    )

def analysis_layout():
    return rx.box(
        rx.vstack(
            rx.heading("Analysis Report", size="6"),
            rx.hstack(
                rx.box(
                    rx.text("Original Code", weight="bold"),
                    rx.text_area(
                        value=AnalyzeState.result.get("original_code", ""),
                        width="100%",
                        height="300px",
                        read_only=True,
                    ),
                    rx.button(
                        "Download Original Code",
                        on_click=lambda: rx.download(
                            AnalyzeState.result.get("original_code", ""),
                            filename="original_code.py"
                        ),
                        margin_top="10px",
                        color_scheme="purple"
                    ),
                    flex="1",
                    padding="10px"
                ),
                rx.box(
                    rx.text("Corrected Code", weight="bold"),
                    rx.text_area(
                        value=AnalyzeState.result.get("corrected_code", ""),
                        width="100%",
                        height="300px",
                        read_only=True,
                    ),
                    rx.hstack(
                        rx.button(
                            "Copy Corrected Code",
                            on_click=[
                                lambda: rx.set_clipboard(AnalyzeState.result.get("corrected_code", "")),
                                lambda: rx.toast("✅ Corrected code copied!", duration=2000)
                            ],
                            color_scheme="blue"
                        ),
                        rx.button(
                            "Download Corrected Code",
                            on_click=lambda: rx.download(
                                AnalyzeState.result.get("corrected_code", ""),
                                filename="corrected_code.py"
                            ),
                            color_scheme="purple"
                        ),
                        spacing="3",
                        margin_top="10px"
                    ),
                    flex="1",
                    padding="10px"
                ),
                spacing="4",
            ),
            spacing="4",
            align="start"
        ),
        flex="1",
        padding="30px",
        background_color="#12121c",
        color="white"
    )



# ✅ Register pages
app = rx.App()
app.add_page(app_layout, route="/")             # Code Editor
app.add_page(analysis_layout, route="/analyze") # Analysis Report
app.add_page(assistant_layout, route="/assistant") # AI Assistant
"""
"""
import reflex as rx
from AI_driven_code_reviewer.components.navbar import navbar  # Assuming you have a navbar function in navbar.py
from AI_driven_code_reviewer.components.hero import hero
from AI_driven_code_reviewer.components.footer import footer
from AI_driven_code_reviewer.components.analyze import analyze_page
from AI_driven_code_reviewer.components.assistant import assistant_page # This is your Chat Assistant
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.container(
                hero(),
                size="4", # Keeps content centered and readable
                padding_top="5em",
                padding_bottom="5em",
            ),
        ),
        rx.divider(width="80%", margin_x="auto"),
        footer(),
        background_color=rx.color("gray", 1), # Soft professional background
        min_height="100vh",
    )

app = rx.App(
    theme=rx.theme(
        appearance="dark", 
        has_background=True, 
        accent_color="indigo",
        radius="large",
    )
)
app.add_page(index,route="/")
def hero():
    return rx.flex(
        rx.vstack(
            #rx.badge("Powered by Gemini 3", variant="soft", color_scheme="indigo"),
            rx.heading("Review Your Code with AI", size="9", weight="bold"),
            rx.text(
                "Detect bugs, improve code quality, and get instant suggestions.",
                size="5",
                color_scheme="gray",
            ),
            rx.link(
                rx.button("Get Started", size="4", variant="solid"),
                href="/analyze"
            ),
            spacing="5",
            align_items="start",
            flex="1",
        ),
        rx.image(
            src="/Chat bot-rafiki.svg", # Ensure this is in your /assets folder
            width="400px",
            height="auto",
            border_radius="15px",
        ),
        flex_direction=["column", "column", "row"], # Responsive: stack on mobile
        spacing="5",
        padding="40px",
        align="center",
    )
def footer():
    return rx.vstack(
        rx.divider(),
        rx.hstack(
            rx.link("About", href="/about", color_scheme="gray"),
            rx.link("GitHub", href="https://github.com", color_scheme="gray"),
            rx.link("Contact", href="/contact", color_scheme="gray"),
            spacing="5",
        ),
        rx.text("© 2026 AI Code Reviewer", size="2", color_scheme="gray"),
        padding="40px",
        align="center",
        width="100%",
    )
# 1. Define the Page Function (Renamed to avoid conflicts)
def main_index() -> rx.Component:
    # Ensure these are calling the functions from your imports
    return rx.box(
        navbar(),
        rx.container(
            hero(),
            size="4",
        ),
        footer(),
    )

# 2. Initialize the App (Keep this name 'app')
app = rx.App()

# 3. Add the Pages (Reference the function name without parentheses)
app.add_page(main_index, route="/")
app.add_page(analyze_page, route="/analyze")
app.add_page(assistant_page, route="/assistant")
#app = rx.App
#app.add_page(index, route="/")
#app.add_page(analyze_page, route="/analyze")
"""
"""
import reflex as rx
from .components.navbar import navbar
from .components.hero import hero
from .components.footer import footer

def index() -> rx.Component:
    return rx.vstack(
        #navbar(),      # <-- Uncomment first, if it crashes, fix navbar.py
         #hero(),      # <-- Uncomment second
         footer(),    # <-- Uncomment third
        rx.heading("Checking Components..."),
        spacing="5",
    )

app = rx.App()
app.add_page(index, route="/")
"""
import reflex as rx
from .components.navbar import navbar
from .components.footer import footer

# Import the two separate page functions
# Ensure these files (analyze.py and assistant.py) exist in your components folder
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