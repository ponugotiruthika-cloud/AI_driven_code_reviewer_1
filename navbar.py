
import reflex as rx

def navbar():
    return rx.box(
        rx.hstack(
            rx.link(
                rx.heading("AI Code Reviewer", size="6", color_scheme="indigo"),
                href="/",  # Clicking the title goes Home
                text_decoration="none",
            ),
            rx.spacer(),
            rx.hstack(
                rx.link(
                    rx.text("Home", weight="medium"),
                    href="/",
                ),
                rx.link(
                    rx.text("AI Assistant", weight="medium"),
                    href="/assistant",
                ),
                # --- NEW HISTORY LINK ---
                rx.link(
                    rx.text("History", weight="medium"),
                    href="/history",
                ),
                rx.link(
                    rx.button("Get Started", variant="soft", color_scheme="indigo"),
                    href="/analyze",
                ),
                spacing="6",
                align="center",
            ),
            justify="between",
            padding_x="2em",
            padding_y="1em",
            width="100%",
        ),
        border_bottom="1px solid #f0f0f0", # Adds a subtle line under the nav
        width="100%",
    )
