r"""Contains the authentication logic of the app."""

# Standard library

# Third party
import streamlit as st
from streamlit_passwordless import BitwardenPasswordlessVerifiedUser
from streamlit_passwordless.components.config import SK_BP_VERIFIED_USER

# Local
from .config import Pages


def is_authenticated(
    redirect: bool = False,
) -> tuple[bool, BitwardenPasswordlessVerifiedUser | None]:
    r"""Check if a user is authenticated.

    Parameters
    ----------
    redirect : bool, default False
        If True the user will be redirected to the sign in and register page
        if the user is not authenticated. If False the function will return
        True or False if the user is authenticated or not and the user object.

    Returns
    -------
    bool
        True if the user is authenticated and False otherwise.

    BitwardenPasswordlessVerifiedUser or None
        The user object. None is returned if the user has not attempted to sign in yet.
    """

    verified_user = st.session_state.get(SK_BP_VERIFIED_USER)

    if verified_user is None or not verified_user.success:
        if redirect:
            st.switch_page(Pages.REGISTER_AND_SIGN_IN)
        else:
            return False, verified_user
    else:
        return True, verified_user


def sign_out() -> None:
    r"""Sign out the authenticated user."""

    st.session_state[SK_BP_VERIFIED_USER] = None
