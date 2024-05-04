r"""Button components."""

# Standard library
from typing import Literal

# Third party
import streamlit as st

# Local
from ..auth import sign_out
from . import ids


def sign_out_button(
    label: str = 'Sign out', button_type: Literal['primary', 'secondary'] = 'primary'
) -> bool:
    r"""A button to sign out the user.

    Parameters
    ----------
    label : str, default 'Sign out'
        The label of the button.

    button_type : Literal['primary', 'secondary'], default 'primary'
        The styling of the button.

    Returns
    -------
    bool
        True if the button was clicked and False otherwise.
    """

    return st.button(label=label, on_click=sign_out, key=ids.SIGN_IN_OUT_BUTTON, type=button_type)
