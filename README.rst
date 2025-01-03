streamlit-passwordless-app
==========================

|Streamlit|


A Streamlit application to showcase the `streamlit-passwordless`_ library.

.. _streamlit-passwordless: https://github.com/antonlydell/streamlit-passwordless


Installation
------------

Install the project to run it locally:

.. code-block:: bash

   ~ $ mkdir stp_app && cd stp_app
   ~/stp_app $ git clone https://github.com/antonlydell/streamlit-passwordless-app.git .
   ~/stp_app $ python -m venv .venv
   ~/stp_app $ source .venv/bin/activate
   ~/stp_app (.venv) $ python -m pip install -r requirements.txt

On Windows you should replace with ``source .venv/bin/activate`` with ``./.venv/bin/Activate.ps1``.
Create an account with `Bitwarden Passwordless.dev`_ if you do not already have one and then
create a local (``~/stp_app/.streamlit/secrets.toml``) or global (``~/.streamlit/secrets.toml``)
`Streamlit secrets`_ file. Paste the contents below into the file:

.. _Bitwarden Passwordless.dev: https://admin.passwordless.dev/Account/Login
.. _Streamlit secrets: https://docs.streamlit.io/develop/api-reference/connections/secrets.toml

.. code-block:: toml

   [streamlit-passwordless]
   STP_BWP_PUBLIC_KEY = '<PUBLIC_KEY>'
   STP_BWP_PRIVATE_KEY = '<PRIVATE_KEY>'
   STP_DB_URL = '<DB_URL>'


``<PUBLIC_KEY>`` and ``<PRIVATE_KEY>`` should be replaced by the public key and private key
of your Bitwarden Passwordless.dev account respectively. The *private key* is called *secret key*
in Bitwarden Passwordless.dev. Replace ``<DB_URL>`` with the `SQLAlchemy database URL`_ of the
streamlit-passwordless user database. Specifying ``STP_DB_URL`` is optional and if not specified
a SQLite database (*streamlit_passwordless.db*) located in the current working directory is used.

.. _SQLAlchemy database URL : https://docs.sqlalchemy.org/en/20/core/engines.html#database-urls


Run the app with the command:

.. code-block:: bash

   ~/stp_app (.venv) $ python -m streamlit run main.py

   You can now view your Streamlit app in your browser.

   Local URL: http://localhost:8501


Open the url in your favorite web browser if it does not open automatically.


License
-------

streamlit-passwordless-app is distributed under the `MIT-license`_.

.. _MIT-license: https://opensource.org/licenses/mit-license.php


.. |Streamlit| image:: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
   :alt: Streamlit Passwordless on Streamlit Community Cloud
   :scale: 100%
   :target: https://passwordless.streamlit.app
