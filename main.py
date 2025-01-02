r"""The home page of the app and the main entry point to run the app."""

# Standard library

# Third party
import streamlit as st
import streamlit_passwordless as stp

# Local
from streamlit_passwordless_app.config import (
    APP_HOME_PAGE_URL,
    APP_ISSUES_PAGE_URL,
    MAINTAINER_INFO,
    STP_GITHUB_URL,
)
from streamlit_passwordless_app.controllers.home import controller

ABOUT = f"""**The [streamlit-passwordless]({STP_GITHUB_URL}) showcase app**

The streamlit-passwordless package provides a user model for Streamlit applications based
on the Bitwarden passwordless technology. It allows users to securely register and sign in
to a Streamlit application using the passkey FIDO2 and WebAuthn protocols.

*The project is under development and not ready for production yet.*
"""

ABOUT_PAGE_CONFIG = f'{ABOUT}\n{MAINTAINER_INFO}'


def app() -> None:
    r"""The main function to run the home page of the app."""

    st.set_page_config(
        page_title='Streamlit Passwordless',
        page_icon=':key:',
        layout='centered',
        menu_items={
            'Get Help': APP_HOME_PAGE_URL,
            'Report a bug': APP_ISSUES_PAGE_URL,
            'About': ABOUT_PAGE_CONFIG,
        },
    )

    _, session_factory, client = stp.setup(create_database=True)

    controller(about=ABOUT)


if __name__ == "__main__":
    app()
