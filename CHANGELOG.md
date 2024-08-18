# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]


## [2.0.0] - 2024-08-18

Support for streamlit-passwordless user database!

The application can now work with the streamlit-passwordless user database that was introduced in
streamlit-passwordless [v0.6.0](https://github.com/antonlydell/streamlit-passwordless/releases/tag/v0.6.0).
The configuration now requires the key `STP_DB_URL` with the SQLAlchemy database url to the streamlit-passwordless
user database. Added improvements to the application's configuration management.


### Added

- `config.ConfigManager` : The configuration manager that manages the application's configuration.

- `config.setup` : Setup the resources needed by the application.


### Changed

- `config.load_bitwarden_passwordless_credentials` : The function now loads the application's
  configuration and not just the credentials for Bitwarden Passwordless.dev.
  Renamed function to `load_config`.

- `config.create_bitwarden_passwordless_client` : The private and public key to
  Bitwarden Passwordless.dev are now input as parameters. The function is now cached with
  `st.cache_data` to ensure each user gets a unique instance of `streamlit_passwordless.BitwardenPasswordlessClient`
  and its underlying `requests.Session` object.


## [1.1.0] - 2024-05-15

Register and sign in from an iPhone!

Issue  [#2 iPhone : Client error "The document is not focused"](https://github.com/antonlydell/streamlit-passwordless-app/issues/2)
is resolved in [streamlit-passwordless v0.4.0](https://github.com/antonlydell/streamlit-passwordless/tree/v0.4.0).


### Changed

- The alias field is removed from the sign in form since it appeared confusing to the user whether
  the field should be filled in or not in order to sign in. Auto discovery of available passkeys is
  used and the alias field is redundant.


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


[Unreleased]: https://github.com/antonlydell/streamlit-passwordless-app/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/antonlydell/streamlit-passwordless-app/releases/tag/v2.0.0
[1.1.0]: https://github.com/antonlydell/streamlit-passwordless-app/releases/tag/v1.1.0
[1.0.1]: https://github.com/antonlydell/streamlit-passwordless-app/releases/tag/v1.0.1
[1.0.0]: https://github.com/antonlydell/streamlit-passwordless-app/releases/tag/v1.0.0
