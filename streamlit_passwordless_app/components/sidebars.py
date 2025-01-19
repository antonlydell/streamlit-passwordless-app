r"""The sidebar components."""

# Standard library

# Third party
import streamlit as st
import streamlit_passwordless as stp

# Local
from streamlit_passwordless_app.config import Pages


def sidebar(user: stp.User | None) -> None:
    r"""Render the sidebar of the application.

    Parameters
    ----------
    user : streamlit_passwordless.User or None
        The signed in user. If None the user has not signed in yet.
    """

    if user is None or not user.is_authenticated:
        return

    with st.sidebar:
        clicked, _ = stp.sign_out_button()
        if clicked:
            return
        st.divider()
        st.markdown('### Navigation')
        st.page_link(page=Pages.HOME, label='Home')
        st.page_link(page=Pages.REGISTER_AND_SIGN_IN, label='Register and Sign in')
        st.divider()
