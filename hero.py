"""
import reflex as rx

def hero():
    return rx.hstack(
                rx.vstack(
                    rx.heading("Review Your Code with AI",size="8"),
                    rx.text("Defect bugs,improve code quality,and get instant suggestions."),
                    rx.hstack(
                        
                    rx.link(rx.button("Try Demo",variant="outline"),href="/analyze"),

            ),
                spacing="5",

        ),rx.image(" Chat bot-rafiki.svg"),
        spacing="1",
        padding="40px",
        align="center"
        )
        """
"""
import reflex as rx

def hero():
    return rx.hstack(
        rx.vstack(
            rx.heading("Review Your Code with AI", size="8"),
            rx.text("Detect bugs, improve code quality, and get instant suggestions."),
            #rx.hstack(
                rx.link(
                    rx.button(rx.button("Get Started", size="3", variant="solid", color_scheme="indigo")),
                    href="/analyze",
                #),
            ),
            spacing="4",
        ),
        rx.image("Chat bot-rafiki.svg" ),
        spacing="5",
        padding="40px",
        align="center"
    ),
    """
import reflex as rx

def hero():
    return rx.hstack(
        rx.vstack(
            rx.heading("Review Your Code with AI", size="8"),
            rx.text("Detect bugs and optimize your code instantly."),
            rx.link(
                rx.button(
                    "Get Started", 
                    size="3", 
                    variant="solid", 
                    color_scheme="indigo"
                ),
                href="/analyze",
            ),
            spacing="4",
            align_items="start",
        ),
        rx.image(
            src="/Chat bot-rafiki.svg", 
            width="400px", 
            height="auto"
        ),
        justify="between",
        width="100%",
    )
    