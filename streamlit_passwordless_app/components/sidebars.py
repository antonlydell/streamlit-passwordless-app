r"""The sidebar components."""

# Standard library

# Third party
import streamlit as st

# Local
from streamlit_passwordless_app.config import Pages

from .buttons import sign_out_button


def sidebar(is_authenticated: bool = False) -> None:
    r"""Render the sidebar of the application.

    Parameters
    ----------
    is_authenticated : bool, default False
        If True the user is authenticated and the sidebar should be rendered
        otherwise the sidebar is not rendered.
    """

    if not is_authenticated:
        return

    with st.sidebar:
        if sign_out_button():
            return
        st.divider()
        st.markdown('### Navigation')
        st.page_link(page=Pages.HOME, label='Home')
        st.page_link(page=Pages.REGISTER_AND_SIGN_IN, label='Register and Sign in')
        st.divider()
