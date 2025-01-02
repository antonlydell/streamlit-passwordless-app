r"""The views of the home page."""

# Standard library

# Third party
import pandas as pd
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


def user_info_section(user: stp.User | None) -> None:
    r"""Render the details about the signed in user.

    Parameters
    ----------
    user : streamlit_passwordless.User or None
        The signed in user or None if the user is not signed in.
    """

    if user is None:
        return

    user_info = ['Username', 'Displayname', 'Role']
    data = [user.username, user.displayname, user.role.name]

    if (sign_in := user.sign_in) is not None:
        sign_in_timestamp = sign_in.sign_in_timestamp.strftime(r'%Y-%m-%d %H:%M:%S %Z')
        user_info.extend(
            ('Sign in Timestamp', 'Credential Nickname', 'Device', 'Country', 'Sign in Type')
        )
        data.extend(
            (
                sign_in_timestamp,
                sign_in.credential_nickname,
                sign_in.device,
                sign_in.country,
                sign_in.sign_in_type,
            )
        )

    index_col = 'User Details'
    df = pd.DataFrame({index_col: user_info, 'Value': data}).set_index(index_col)

    st.dataframe(df, use_container_width=True)
