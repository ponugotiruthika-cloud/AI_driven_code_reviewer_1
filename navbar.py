"""
import reflex as rx

def navbar():
    return rx.hstack(
        rx.center(
            rx.icon('Chat bot-rafiki.svg'),
            rx.text("AI Code Reviewer",font_weight='bold',align="center",)
            

        ),
        rx.spacer(),
        rx.hstack(
            rx.link("home",href='/'),
            rx.link("analyze",href='/analyz'),
            rx.link("history",href='/history'),
            rx.link("about",href='/about'),
            spacing='5'   
        ),
          padding='20px',
        width="100%",

    )
   """
 
"""
import reflex as rx

def navbar():
    rx.button("Menu"),
    rx.divider(orientation="vertical")
    return rx.flex(
            rx.box(
            rx.image(src='Chat bot-rafiki.png',
                        width='100px', align="start")
    ),
    rx.menu.root(
        rx.menu.trigger(
            rx.button('Menu')
        ),
        rx.menu.content(
            rx.menu.item(
                rx.link('About', href='/about')),
            rx.menu.item(
                rx.link('posts', href= '/posts'),
            ))
        ),
        justify='start',
        width='100%',
        padding='20px'
    )
"""
       
"""
import reflex as rx

def navbar():
    return rx.hstack(
        rx.button("Menu"),
        rx.divider(orientation="vertical"),
        rx.hstack(
            rx.link("About", href="/about"),
            rx.link("GitHub", href="https://github.com"),
            rx.link("Contact", href="/contact"),
            spacing="4",
        ),
        spacing="4",
        padding="10px",
    )
"""
"""
import reflex as rx

def navbar():
    return rx.hstack(
        rx.hstack(
            # Use image instead of icon for your custom SVG logo
            rx.image(src="/Chat bot-rafiki.svg", width="30px", height="auto"),
            rx.text("AI Code Reviewer", font_weight='bold'),
            align="center",
            spacing="2",
        ),
        rx.spacer(),
        rx.hstack(
            # This "href='/'" tells Reflex to go to the main index page
            rx.link("Home", href="/"), 
            rx.link("AI Assistant", href="/AI Assistant"),
            rx.link("History", href="/history"),
            rx.link("About", href="/about"),
            spacing='5'   
        ),
        padding='20px',
        width="100%",
        # This keeps the navbar stuck to the top
        position="sticky",
        top="0",
        z_index="999",
        background_color=rx.color("gray", 2),
    )
 """
"""
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
    """

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