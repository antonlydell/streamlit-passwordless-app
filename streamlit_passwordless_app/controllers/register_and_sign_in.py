r"""The page controller of the register and sign in page."""

# Standard library

# Third party
import streamlit as st
import streamlit_passwordless as stp

# Local
from streamlit_passwordless_app.components.sidebars import sidebar
from streamlit_passwordless_app.views.home import title
from streamlit_passwordless_app.views.register_and_sign_in import register_and_sign_in_section


def controller(client: stp.BitwardenPasswordlessClient, db_session: stp.db.Session) -> None:
    r"""Render the register and sign in page.

    Parameters
    ----------
    client : streamlit_passwordless.BitwardenPasswordlessClient
        The client to communicate with the Bitwarden Passwordless.dev API.

    db_session : streamlit_passwordless.db.Session
        An active session to the streamlit-passwordless user database.
    """

    title()
    register_and_sign_in_section(client=client, db_session=db_session)
    sidebar(user=st.session_state.get(stp.SK_USER))
