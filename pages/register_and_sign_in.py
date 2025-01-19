r"""The register and sign in page of the app."""

# Standard library
import logging

# Third party
import streamlit as st
import streamlit_passwordless as stp

# Local
from streamlit_passwordless_app.config import (
    APP_HOME_PAGE_URL,
    APP_ISSUES_PAGE_URL,
    MAINTAINER_INFO,
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

    client, session_factory, _ = stp.setup(create_database=True)

    with session_factory() as session:
        stp.db.init(_session=session)
        controller(client=client, db_session=session)


if __name__ == "__main__":
    main()
