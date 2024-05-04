r"""The register and sign in page of the app."""

# Standard library
import logging

# Third party
import streamlit as st
import streamlit_passwordless as stp

from streamlit_passwordless_app.config import (
    APP_HOME_PAGE_URL,
    APP_ISSUES_PAGE_URL,
    MAINTAINER_INFO,
    create_bitwarden_passwordless_client,
)
from streamlit_passwordless_app.controllers.register_and_sign_in import controller

logger = logging.getLogger(__name__)

ABOUT = f"""The register and sign in page of the app.

Allows the user to register an account with the app by creating and registring a passkey
with the user's device. The user can also sign in to the app with the created passkey.

{MAINTAINER_INFO}
"""


def main() -> None:
    r"""The main function to run the register and sign in page of the app."""

    st.set_page_config(
        page_title='Streamlit Passwordless - Sign In',
        page_icon=':lock:',
        layout='centered',
        menu_items={
            'Get Help': APP_HOME_PAGE_URL,
            'Report a bug': APP_ISSUES_PAGE_URL,
            'About': ABOUT,
        },
    )

    if not st.session_state:
        stp.init_session_state()

    try:
        client = create_bitwarden_passwordless_client()
    except stp.StreamlitPasswordlessError as e:
        logger.error(str(e))
        st.error('Error creating BitwardenPasswordlessClient!', icon=stp.ICON_ERROR)
        return

    controller(client=client)


if __name__ == "__main__":
    main()
