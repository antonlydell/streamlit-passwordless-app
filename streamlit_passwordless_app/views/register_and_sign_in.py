r"""The views of the register and sign in page."""

# Standard library

# Third party
import streamlit as st
import streamlit_passwordless as stp

# Local


def register_and_sign_in_section(client: stp.BitwardenPasswordlessClient) -> None:
    r"""Render the forms to register and sign in to the application."""

    register_tab, signin_in_tab = st.tabs(["Register", "Sign in"])
    with register_tab:
        stp.bitwarden_register_form(client=client)
    with signin_in_tab:
        stp.bitwarden_sign_in_form(client=client, with_alias=False)
