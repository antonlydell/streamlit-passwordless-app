r"""The page controller of the home page."""

# Standard library

# Third party
import streamlit as st
import streamlit_passwordless as stp

# Local
from streamlit_passwordless_app.auth import is_authenticated
from streamlit_passwordless_app.components.sidebars import sidebar
from streamlit_passwordless_app.views.home import (
    streamlit_passwordless_info_section,
    title,
    user_info_section,
)


def controller(
    client: stp.BitwardenPasswordlessClient, db_session: stp.db.Session, about: str
) -> None:
    r"""Render the home page.

    Parameters
    ----------
    client : streamlit_passwordless.BitwardenPasswordlessClient
        The client to communicate with the Bitwarden Passwordless.dev API.

    db_session : streamlit_passwordless.db.Session
        An active session to the streamlit-passwordless user database.

    about : str
        The text about the streamlit-passwordless library to render
        in the streamlit-passwordless info section.
    """

    authenticated, user = is_authenticated(redirect=True)
    sidebar(is_authenticated=authenticated)
    title()
    streamlit_passwordless_info_section(text=about)

    left_col, right_col = st.columns([0.6, 0.4])
    with left_col:
        user_info_section(user=user)
    with right_col:
        stp.bitwarden_register_form_existing_user(
            client=client,
            db_session=db_session,
            with_discoverability=True,
            title='#### Register a new passkey',
        )
