r"""Contains the configuration of the app."""

# Standard library
from enum import StrEnum

# Local
from streamlit_passwordless_app import __releasedate__, __version__

MAINTAINER_INFO = f"""\
- Maintainer   : [*Anton Lydell*](https://github.com/antonlydell)
- Version      : {__version__}
- Release date : {__releasedate__}"""


# =====================================================================================
# URL:s
# =====================================================================================

APP_HOME_PAGE_URL = 'https://github.com/antonlydell/streamlit-passwordless-app'
APP_ISSUES_PAGE_URL = 'https://github.com/antonlydell/streamlit-passwordless-app/issues'
BITWARDEN_PASSWORDLESS_URL = 'https://bitwarden.com/products/passwordless'
STP_GITHUB_URL = 'https://github.com/antonlydell/streamlit-passwordless'


# =====================================================================================
# Pages
# =====================================================================================


class Pages(StrEnum):
    r"""The pages of the application."""

    HOME = 'main.py'
    REGISTER_AND_SIGN_IN = 'pages/register_and_sign_in.py'
