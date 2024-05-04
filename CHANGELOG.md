# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]


## [1.0.1] - 2024-05-04

Deployed to Streamlit Community Cloud!


### Fixed

- **Deployment error on Streamlit Community Cloud** : Moved the `main.py` file and the pages directory
  from the `streamlit_passwordless_app` package to the root level of the project directory. This resolved
  the deployment error on Streamlit Community Cloud, where you need to have the entry point Python file
  at the root level of the project to make the app run. The pages' directory has to be on the same level
  as the entry point file.


## [1.0.0] - 2024-05-04

A first release of the app!

The user can register an account with the app by creating and registering a passkey with the user's
device. The user can also sign in to the app with the created passkey. After successful registration
and sign in a simple view on the home page of the app is available to the user with info about the
[streamlit-passwordless](https://github.com/antonlydell/streamlit-passwordless) library and the
signed in user. In the sidebar there is a button to sign out from the app.


[Unreleased]: https://github.com/antonlydell/streamlit-passwordless-app/compare/v1.0.1...HEAD
[1.0.1]: https://github.com/antonlydell/streamlit-passwordless-app/releases/tag/v1.0.1
[1.0.0]: https://github.com/antonlydell/streamlit-passwordless-app/releases/tag/v1.0.0
