r"""The views of the register and sign in page."""

# Standard library

# Third party
import streamlit as st
import streamlit_passwordless as stp

# Local
from streamlit_passwordless_app.config import Pages


def register_and_sign_in_section(
    client: stp.BitwardenPasswordlessClient, db_session: stp.db.Session
) -> None:
    r"""Render the forms to register and sign in to the application.

    Parameters
    ----------
    client : streamlit_passwordless.BitwardenPasswordlessClient
        The client to communicate with the Bitwarden Passwordless.dev API.

    db_session : streamlit_passwordless.db.Session
        An active session to the streamlit-passwordless user database.
    """

    with st.container(border=True):
        stp.bitwarden_register_form(
            client=client, db_session=db_session, with_displayname=True, border=False
        )
        st.divider()
        st.write('Already have an account?')
        stp.bitwarden_sign_in_button(client=client, db_session=db_session, redirect=Pages.HOME)
