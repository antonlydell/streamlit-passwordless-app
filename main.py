r"""The home page of the app and the main entry point to run the app."""

# Standard library

# Third party
import streamlit as st
import streamlit_passwordless as stp

# Local
from streamlit_passwordless_app.config import (
    APP_HOME_PAGE_URL,
    APP_ISSUES_PAGE_URL,
    BITWARDEN_PASSWORDLESS_URL,
    MAINTAINER_INFO,
    STP_GITHUB_URL,
    Pages,
)
from streamlit_passwordless_app.controllers.home import controller

ABOUT = f"""**The [Streamlit Passwordless]({STP_GITHUB_URL}) showcase app**

Streamlit Passwordless provides a user model for Streamlit applications with a passkey
authentication workflow based on [Bitwarden Passwordless.dev]({BITWARDEN_PASSWORDLESS_URL}),
which allows users to easily and securely register passkeys and sign in to an application.
Streamlit Passwordless also provides a user role system to implement authorized access to
certain pages or functions within an application.

*The project is under development and not ready for production yet.*
"""

ABOUT_PAGE_CONFIG = f'{ABOUT}\n{MAINTAINER_INFO}'


@stp.authorized(redirect=Pages.REGISTER_AND_SIGN_IN)
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

    client, session_factory, _ = stp.setup(create_database=True)

    with session_factory() as session:
        stp.db.init(_session=session)
        controller(client=client, db_session=session, about=ABOUT)


if __name__ == "__main__":
    app()
