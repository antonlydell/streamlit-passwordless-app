r"""The views of the home page."""

# Standard library

# Third party
import streamlit as st
import streamlit_passwordless as stp


def title() -> None:
    r"""Render the main title section of the application."""

    st.title('Streamlit Passwordless')
    st.subheader('Next Level Security for Next Level Applications')
    st.divider()


def streamlit_passwordless_info_section(text: str) -> None:
    r"""Render the info section about the streamlit-passwordless library."""

    st.markdown(text)
    st.divider()


def user_details_list(
    user: stp.BitwardenPasswordlessVerifiedUser, header: str | None = '## User Info'
) -> None:
    r"""Render the user details in a list form."""

    sign_in_timestamp = user.sign_in_timestamp.strftime(r'%Y-%m-%d %H:%M:%S %Z')
    st.markdown(
        f"""{header}
- **UserName** : {user.credential_nickname}
- **UserId** : {user.user_id}
- **Sign in timestamp** : {sign_in_timestamp}
- **Device** : {user.device}
- **Country** : {user.country}"""
    )
    st.divider()
