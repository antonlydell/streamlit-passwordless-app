r"""The views of the register and sign in page."""

# Standard library

# Third party
import streamlit as st
import streamlit_passwordless as stp


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

    register_tab, signin_in_tab = st.tabs(["Register", "Sign in"])
    with register_tab:
        stp.bitwarden_register_form(
            client=client, db_session=db_session, username_placeholder='john_doe'
        )
    with signin_in_tab:
        stp.bitwarden_sign_in_form(client=client, db_session=db_session, with_alias=False)
