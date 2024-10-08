r"""Contains the configuration of the app."""

# Standard library
import logging
from datetime import timedelta
from enum import StrEnum

# Third party
import streamlit as st
import streamlit_passwordless as stp

# Local
from streamlit_passwordless_app import __releasedate__, __version__

logger = logging.getLogger(__name__)


MAINTAINER_INFO = f"""\
- Maintainer   : [*Anton Lydell*](https://github.com/antonlydell)
- Version      : {__version__}
- Release date : {__releasedate__}"""


# =====================================================================================
# URL:s
# =====================================================================================

APP_HOME_PAGE_URL = 'https://github.com/antonlydell/streamlit-passwordless-app'
APP_ISSUES_PAGE_URL = 'https://github.com/antonlydell/streamlit-passwordless-app/issues'
STP_GITHUB_URL = 'https://github.com/antonlydell/streamlit-passwordless'


# =====================================================================================
# Pages
# =====================================================================================


class Pages(StrEnum):
    r"""The pages of the application."""

    HOME = 'main.py'
    REGISTER_AND_SIGN_IN = 'pages/register_and_sign_in.py'


# =====================================================================================
# Secrets
# =====================================================================================

STP_SECRETS_SECTION = 'streamlit-passwordless'
STP_PUBLIC_KEY = 'STP_PUBLIC_KEY'
STP_PRIVATE_KEY = 'STP_PRIVATE_KEY'
STP_DB_URL = 'STP_DB_URL'


# =====================================================================================
# Configuration
# =====================================================================================


class ConfigManager:
    r"""The configuration manager that manages the application's configuration.

    Parameters
    ----------
    public_key : str
        The public key to Bitwarden Passwordless.dev.

    private_key : str
        The private key to Bitwarden Passwordless.dev.

    db_url : str
        The SQLAlchemy database url to the streamlit-passwordless user database.
    """

    __slots__ = ('public_key', 'private_key', 'db_url')

    def __init__(self, public_key: str, private_key: str, db_url: str) -> None:
        self.public_key = public_key
        self.private_key = private_key
        self.db_url = db_url

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(public_key=***, private_key=***, db_url={self.db_url})'

    def __str__(self) -> str:
        return self.__repr__()


# =====================================================================================
# Functions
# =====================================================================================


@st.cache_resource(ttl=timedelta(days=7), show_spinner=False)
def load_config() -> ConfigManager:
    r"""Load the application's configuration.

    Returns
    -------
    ConfigManager
        The loaded configuration.

    Raises
    ------
    streamlit_passwordless.StreamlitPasswordlessError
        If the required configuration could not be found.
    """

    public_key = st.secrets.get(STP_SECRETS_SECTION, {}).get(STP_PUBLIC_KEY)
    private_key = st.secrets.get(STP_SECRETS_SECTION, {}).get(STP_PRIVATE_KEY)
    db_url = st.secrets.get(STP_SECRETS_SECTION, {}).get(STP_DB_URL)

    if public_key is None or private_key is None:
        error_msg = 'Bitwarden Passwordless credentials not found! Check your configuration.'
        logger.error(error_msg)
        raise stp.StreamlitPasswordlessError(error_msg)

    if db_url is None:
        error_msg = 'streamlit-passwordless database url not found! Check your configuration.'
        logger.error(error_msg)
        raise stp.StreamlitPasswordlessError(error_msg)

    return ConfigManager(private_key=private_key, public_key=public_key, db_url=db_url)


@st.cache_data(ttl=timedelta(days=7), show_spinner=False)
def create_bitwarden_passwordless_client(
    private_key: str, public_key: str
) -> stp.BitwardenPasswordlessClient:
    r"""Create the client to communicate with Bitwarden Passwordless.dev."""

    return stp.BitwardenPasswordlessClient(public_key=public_key, private_key=private_key)


def setup() -> tuple[ConfigManager, stp.BitwardenPasswordlessClient, stp.db.core.SessionFactory]:
    r"""Setup the resources needed by the application."""

    cm = load_config()
    client = create_bitwarden_passwordless_client(
        private_key=cm.private_key, public_key=cm.public_key
    )
    session_factory = stp.db.create_session_factory(url=cm.db_url)

    return cm, client, session_factory
