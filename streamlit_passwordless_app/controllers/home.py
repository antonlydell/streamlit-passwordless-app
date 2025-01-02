r"""The page controller of the home page."""

# Standard library

# Third party

# Local
from streamlit_passwordless_app.auth import is_authenticated
from streamlit_passwordless_app.components.sidebars import sidebar
from streamlit_passwordless_app.views.home import (
    streamlit_passwordless_info_section,
    title,
    user_info_section,
)


def controller(about: str) -> None:
    r"""Render the home page.

    Parameters
    ----------
    about : str
        The text about the streamlit-passwordless library to render
        in the streamlit-passwordless info section.
    """

    authenticated, user = is_authenticated(redirect=True)
    sidebar(is_authenticated=authenticated)
    title()
    streamlit_passwordless_info_section(text=about)
    user_info_section(user=user)
