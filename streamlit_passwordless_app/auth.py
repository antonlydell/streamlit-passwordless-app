r"""Contains the authentication logic of the app."""

# Standard library

# Third party
import streamlit as st
import streamlit_passwordless as stp

# Local
from .config import Pages


def is_authenticated(
    redirect: bool = False,
) -> tuple[bool, stp.UserSignIn | None]:
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

    streamlit_passwordless.UserSignIn or None
        Details from Bitwarden Passwordless about the user that signed in.
        None is returned if the user has not attempted to sign in yet.
    """

    sign_in = st.session_state.get(stp.SK_USER_SIGN_IN)

    if sign_in is None or not sign_in.success:
        if redirect:
            st.switch_page(Pages.REGISTER_AND_SIGN_IN)
        else:
            return False, sign_in
    else:
        return True, sign_in


def sign_out() -> None:
    r"""Sign out the authenticated user."""

    if (user := st.session_state.get(stp.SK_USER)) is not None:
        user.sign_in = None
    st.session_state[stp.SK_USER_SIGN_IN] = None
