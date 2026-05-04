Contrib for ``balderhub-auth``
******************************

For activating this module, you need to install the package like shown below

.. code-block:: none

    >>> pip install balderhub-html[auth]

Once installed you can use it.

Available Processes
===================

Login Process
-------------

This package provides a ready-to-use implementation for login:

To test this workflow, you can use the :class:`balderhub.auth.scenarios.ScenarioSimpleLogin`:


.. code-block:: python

    # file scenario_balderhub_auth.py

    from balderhub.auth.scenarios import ScenarioSimpleLogin


.. code-block:: python

    import balder
    import balderhub.selenium.lib.setup_features


    class SetupLogin(balder.Setup):
        class Server(balder.Device):
            pass

        @balder.connect(Server, over_connection=balder.Connection)
        class Client(balder.Device):
            selenium = balderhub.selenium.lib.setup_features.SeleniumXXWebdriverFeature() # or other feature that supports `balderhub-webdriver`

            role = MyUserRole()
            page_login = LoginPage()

            login = balderhub.html.contrib.auth.setup_features.UserLoginFeature()

This will execute the scenario with your setup:

.. code-block:: none

    +----------------------------------------------------------------------------------------------------------------------+
    | BALDER Testsystem                                                                                                    |
    |  python version 3.10.9 (main, Dec  8 2022, 02:19:14) [GCC 12.2.1 20220924] | balder version 0.2.2                    |
    +----------------------------------------------------------------------------------------------------------------------+
    Collect 1 Setups and 1 Scenarios
      resolve them to 1 valid variations

    ================================================== START TESTSESSION ===================================================
    SETUP SetupLogin
      SCENARIO ScenarioSimpleLogin
        VARIATION ScenarioSimpleLogin.Client:SetupLogin.Client
          TEST ScenarioSimpleLogin.test_login [.]
    ================================================== FINISH TESTSESSION ==================================================
    TOTAL NOT_RUN: 0 | TOTAL FAILURE: 0 | TOTAL ERROR: 0 | TOTAL SUCCESS: 1 | TOTAL SKIP: 0 | TOTAL COVERED_BY: 0

You need an implementation for the following features:

+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Property Name (From Example Setup) | Feature                                                                                            | Description                                             |
+====================================+====================================================================================================+=========================================================+
| ``page_login``                     | :class:`~balderhub.html.contrib.auth.pages.LoginPage`                                              | Page Bindings for the mail login page                   |
|                                    |                                                                                                    |                                                         |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``role``                           | :class:`~balderhub.html.contrib.auth.scenario_features.ExtendedUserRole`                           | Config values for user (username, mail, password, ..)   |
|                                    |                                                                                                    | the login should be done with (needs to exist)          |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+



Registration Processes (All-In-One | Mail-Confirmation over Link)
-----------------------------------------------------------------

The All-In-One Registration Process is widely used by many applications. Within the first view, all information of the
new user (username, mail, password, ..) is requested. After submitting the formular, a mail is sent to the users mail
address. This mail provides a limited-valid link or register token (or both) to complete the registration and confirm
the registration. This package allows both versions: confirming by token or confirming by link. As soon as the token is
provided or the link was opened, the registration is completed and the user is able to log in.

.. list-table:: Process Register All-In-One With Link
   :widths: 10 60 30
   :width: 100%
   :header-rows: 1
   :align: center

   * - **Step**
     - **Wireframe**
     - **Description**
   * - **1**
     - .. image:: /_static/RegistrationAllInOnePage.svg
           :align: center
           :alt: Wireframe of a widely used registration page

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.RegistrationAllInOnePage`

     - Providing all necessary information for the new user
   * - **2**
     - .. image:: /_static/ReceiveMailLink.svg
           :align: center
           :alt: Symbol for waiting for a Mail with an activation link

       .. centered:: :class:`~balderhub.html.contrib.auth.setup_features.MailConfirmationForRegistrationByLinkFeature`

     - Waiting for a mail to the provided email address with a link to complete the registration
   * - **3**
     - .. image:: /_static/RegistrationConfirmationPage.svg
           :align: center
           :alt: Wireframe of a widely used registration page

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.RegistrationConfirmationPage`

     - Confirmation Page, visible when the registration is completed

To test this workflow, you can use the :class:`balderhub.auth.scenarios.ScenarioRegisterNewAsUnauth`:


.. code-block:: python

    # file scenario_balderhub_auth.py

    from balderhub.auth.scenarios import ScenarioRegisterNewAsUnauth


For minimal required setup for the All-In-One Registration process is shown below:

.. code-block:: python

    import balder
    import balder.connections as cnns

    import balderhub.html.contrib.auth.setup_features
    import balderhub.selenium.lib.setup_features
    import balderhub.smtp.lib.setup_features


    class SetupAllInOneRegistration(balder.Setup):
        class Server(balder.Device):
            pass

        class SmtpServer(balder.Device):
            smtp = balderhub.smtp.lib.setup_features.AiosmtpdServerFeature()

        @balder.connect(SmtpServer, over_connection=cnns.SmtpConnection)
        @balder.connect(Server, over_connection=balder.Connection)
        class UnregisteredClient(balder.Device):
            selenium = balderhub.selenium.lib.setup_features.SeleniumXXWebdriverFeature()  # or other feature that supports `balderhub-webdriver`

            role = UnregisteredUserRole()

            page_login = LoginPage()
            login = balderhub.html.contrib.auth.setup_features.UserLoginFeature()

            page_register = RegistrationAllInOnePage()
            page_registration_confirm = RegistrationConfirmationPage()

            registration = balderhub.html.contrib.auth.setup_features.RegisterSelfAllDataAtOnceFeature()

            mail = balderhub.smtp.lib.setup_features.ProxySmtpReader(SmtpServer='SmtpServer')
            mail_confirm = MailConfirmationForRegistrationByLinkFeature()

This will execute the scenario with your setup:

.. code-block:: none

    +----------------------------------------------------------------------------------------------------------------------+
    | BALDER Testsystem                                                                                                    |
    |  python version 3.10.9 (main, Dec  8 2022, 02:19:14) [GCC 12.2.1 20220924] | balder version 0.2.2                    |
    +----------------------------------------------------------------------------------------------------------------------+
    Collect 1 Setups and 1 Scenarios
      resolve them to 1 valid variations

    ================================================== START TESTSESSION ===================================================
    SETUP SetupRegistrationRequestFirst
      SCENARIO ScenarioRegisterNewAsUnauth
        VARIATION ScenarioRegisterNewAsUnauth.Server:SetupRegistrationRequestFirst.Server | ScenarioRegisterNewAsUnauth.UnauthClient:SetupRegistrationRequestFirst.UnregisteredClient
          TEST ScenarioRegisterNewAsUnauth.test_register_new_user [.]
    ================================================== FINISH TESTSESSION ==================================================
    TOTAL NOT_RUN: 0 | TOTAL FAILURE: 0 | TOTAL ERROR: 0 | TOTAL SUCCESS: 1 | TOTAL SKIP: 0 | TOTAL COVERED_BY: 0


You need an implementation for the following features:

+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Property Name (From Example Setup) | Feature                                                                                            | Description                                             |
+====================================+====================================================================================================+=========================================================+
| ``role``                           | :class:`~balderhub.html.contrib.auth.scenario_features.ExtendedUserRole`                           | Config values for user (username, mail, password, ..)   |
|                                    |                                                                                                    | that should be used for registration (mail/username     |
|                                    |                                                                                                    | needs to be unused)                                     |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_register``                  | :class:`~balderhub.html.contrib.auth.pages.RegistrationAllInOnePage`                               | Page Bindings to the main registration page             |
|                                    |                                                                                                    |                                                         |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``mail_confirm``                   | :class:`~balderhub.html.contrib.auth.setup_features.MailConfirmationForRegistrationByLinkFeature`  | Features provides constructions how the link can        |
|                                    |                                                                                                    | be extracted from mail / mail content is validated      |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_registration_confirm``      | :class:`~balderhub.html.contrib.auth.pages.RegistrationConfirmationPage`                           | Page Bindings to the normal confirmation page after the |
|                                    |                                                                                                    | registration was successfully executed                  |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_login``                     | :class:`~balderhub.html.contrib.auth.pages.LoginPage`                                              | Page Bindings for the login page - necessary for        |
|                                    |                                                                                                    | validating if the registration was successful and user  |
|                                    |                                                                                                    | can log in afterwards                                   |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+

.. note::
    The scenario :class:`balderhub.auth.scenarios.ScenarioRegisterNewAsUnauth` does not provide a clean up fixture.
    Make sure, this is be handled within your setup fixtures.

Registration Processes (All-In-One | Mail-Confirmation over Token)
------------------------------------------------------------------

.. list-table:: Process Register All-In-One With Token
   :widths: 10 60 30
   :width: 100%
   :header-rows: 1
   :align: center

   * - **Step**
     - **Wireframe**
     - **Description**
   * - **1**
     - .. image:: /_static/RegistrationAllInOnePage.svg
           :align: center
           :alt: Wireframe of a widely used registration page

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.RegistrationAllInOnePage`

     - Providing all necessary information for the new user
   * - **2**
     - .. image:: /_static/ReceiveMailToken.svg
           :align: center
           :alt: Symbol for waiting for a Mail with an activation link

       .. centered:: :class:`~balderhub.html.contrib.auth.setup_features.MailConfirmationForRegistrationByTokenFeature`

     - Waiting for a mail to the provided email address with a link to complete the registration
   * - **3**
     - .. image:: /_static/RegistrationInsertTokenPage.svg
           :align: center
           :alt: Wireframe of a Page, that expects the token received by mail after registration

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.RegistrationInsertTokenPage`

     - Confirmation Page, visible when the registration is completed
   * - **4**
     - .. image:: /_static/RegistrationConfirmationPage.svg
           :align: center
           :alt: Wireframe of a widely used registration page

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.RegistrationConfirmationPage`

     - Confirmation Page, visible when the registration is completed

To test this workflow, you can use the :class:`balderhub.auth.scenarios.ScenarioRegisterNewAsUnauth`:


.. code-block:: python

    # file scenario_balderhub_auth.py

    from balderhub.auth.scenarios import ScenarioRegisterNewAsUnauth


For minimal required setup for the All-In-One Registration process is shown below:

.. code-block:: python

    import balder
    import balder.connections as cnns

    import balderhub.html.contrib.auth.setup_features
    import balderhub.selenium.lib.setup_features
    import balderhub.smtp.lib.setup_features


    class SetupAllInOneRegistration(balder.Setup):
        class Server(balder.Device):
            pass

        class SmtpServer(balder.Device):
            smtp = balderhub.smtp.lib.setup_features.AiosmtpdServerFeature()

        @balder.connect(SmtpServer, over_connection=cnns.SmtpConnection)
        @balder.connect(Server, over_connection=balder.Connection)
        class UnregisteredClient(balder.Device):
            selenium = balderhub.selenium.lib.setup_features.SeleniumFeature()  # or other feature that supports `balderhub-webdriver`

            role = UnregisteredUserRole()

            page_login = LoginPage()
            login = balderhub.html.contrib.auth.setup_features.UserLoginFeature()

            page_register = RegistrationAllInOnePage()
            page_register_insert_token = RegistrationInsertTokenPage()
            page_registration_confirm = RegistrationConfirmationPage()

            registration = balderhub.html.contrib.auth.setup_features.RegisterSelfAllDataAtOnceFeature()

            mail = balderhub.smtp.lib.setup_features.ProxySmtpReader(SmtpServer='SmtpServer')
            mail_confirm = MailConfirmationForRegistrationByTokenFeature()

This will execute the scenario with your setup:

.. code-block:: none

    +----------------------------------------------------------------------------------------------------------------------+
    | BALDER Testsystem                                                                                                    |
    |  python version 3.10.9 (main, Dec  8 2022, 02:19:14) [GCC 12.2.1 20220924] | balder version 0.2.2                    |
    +----------------------------------------------------------------------------------------------------------------------+
    Collect 1 Setups and 1 Scenarios
      resolve them to 1 valid variations

    ================================================== START TESTSESSION ===================================================
    SETUP SetupRegistrationRequestFirst
      SCENARIO ScenarioRegisterNewAsUnauth
        VARIATION ScenarioRegisterNewAsUnauth.Server:SetupRegistrationRequestFirst.Server | ScenarioRegisterNewAsUnauth.UnauthClient:SetupRegistrationRequestFirst.UnregisteredClient
          TEST ScenarioRegisterNewAsUnauth.test_register_new_user [.]
    ================================================== FINISH TESTSESSION ==================================================
    TOTAL NOT_RUN: 0 | TOTAL FAILURE: 0 | TOTAL ERROR: 0 | TOTAL SUCCESS: 1 | TOTAL SKIP: 0 | TOTAL COVERED_BY: 0


You need an implementation for the following features:

+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Property Name (From Example Setup) | Feature                                                                                            | Description                                             |
+====================================+====================================================================================================+=========================================================+
| ``role``                           | :class:`~balderhub.html.contrib.auth.scenario_features.ExtendedUserRole`                           | Config values for user (username, mail, password, ..)   |
|                                    |                                                                                                    | that should be used for registration (mail/username     |
|                                    |                                                                                                    | needs to be unused)                                     |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_register``                  | :class:`~balderhub.html.contrib.auth.pages.RegistrationAllInOnePage`                               | Page Bindings to the main registration page             |
|                                    |                                                                                                    |                                                         |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_register_insert_token``     | :class:`~balderhub.html.contrib.auth.pages.RegistrationInsertTokenPage`                            | Page Bindings, the token received by mail, needs to be  |
|                                    |                                                                                                    | inserted                                                |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``mail_confirm``                   | :class:`~balderhub.html.contrib.auth.setup_features.MailConfirmationForRegistrationByTokenFeature` | Features provides constructions how the token can       |
|                                    |                                                                                                    | be extracted from mail / mail content is validated      |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_registration_confirm``      | :class:`~balderhub.html.contrib.auth.pages.RegistrationConfirmationPage`                           | Page Bindings to the normal confirmation page after the |
|                                    |                                                                                                    | registration was successfully executed                  |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_login``                     | :class:`~balderhub.html.contrib.auth.pages.LoginPage`                                              | Page Bindings for the login page - necessary for        |
|                                    |                                                                                                    | validating if the registration was successful and user  |
|                                    |                                                                                                    | can log in afterwards                                   |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+

.. note::
    The scenario :class:`balderhub.auth.scenarios.ScenarioRegisterNewAsUnauth` does not provide a clean up fixture.
    Make sure, this is be handled within your setup fixtures.

Registration Processes (Mail First | Mail-Confirmation over Link)
-----------------------------------------------------------------

.. list-table:: Process Register Request-First With Link
   :widths: 10 60 30
   :width: 100%
   :header-rows: 1
   :align: center

   * - **Step**
     - **Wireframe**
     - **Description**
   * - **1**
     - .. image:: /_static/RegistrationRequestPage.svg
           :align: center
           :alt: Wireframe of a Request-Registration Page, that expects the mail to be confirmed before providing more data for registration

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.RegistrationRequestPage`

     - Providing the mail address only
   * - **2**
     - .. image:: /_static/ReceiveMailLink.svg
           :align: center
           :alt: Symbol for waiting for a Mail with an activation link

       .. centered:: :class:`~balderhub.html.contrib.auth.setup_features.MailConfirmationForRegistrationByLinkFeature`

     - Waiting for a mail to the provided email address with a link to complete the registration
   * - **3**
     - .. image:: /_static/RegistrationFinalizationPage.svg
           :align: center
           :alt: Wireframe of the register finalization page, that will be presented when the user confirms the mail address

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.RegistrationFinalizationPage`

     - Finalization Page, visible when the mail is confirmed; form expects remaining registration data
   * - **4**
     - .. image:: /_static/RegistrationConfirmationPage.svg
           :align: center
           :alt: Wireframe of a widely used registration page

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.RegistrationConfirmationPage`

     - Confirmation Page, visible when the registration is completed

To test this workflow, you can use the :class:`balderhub.auth.scenarios.ScenarioRegisterNewAsUnauth`:


.. code-block:: python

    # file scenario_balderhub_auth.py

    from balderhub.auth.scenarios import ScenarioRegisterNewAsUnauth


For minimal required setup for the Request-First Registration process is shown below:

.. code-block:: python

    import balder
    import balder.connections as cnns

    import balderhub.html.contrib.auth.setup_features
    import balderhub.selenium.lib.setup_features
    import balderhub.smtp.lib.setup_features


    class SetupRegistrationRequestFirst(balder.Setup):
        class Server(balder.Device):
            pass

        class SmtpServer(balder.Device):
            smtp = balderhub.smtp.lib.setup_features.AiosmtpdServerFeature()

        @balder.connect(SmtpServer, over_connection=cnns.SmtpConnection)
        @balder.connect(Server, over_connection=balder.Connection)
        class UnregisteredClient(balder.Device):
            selenium = balderhub.selenium.lib.setup_features.SeleniumXXWebdriverFeature()  # or other feature that supports `balderhub-webdriver`

            role = UnregisteredUserRole()

            page_login = LoginPage()
            login = balderhub.html.contrib.auth.setup_features.UserLoginFeature()

            page_req_register = RegistrationRequestPage()
            page_registration_finalize = RegistrationFinalizationPage()
            page_registration_confirm = RegistrationConfirmationPage()

            registration = balderhub.html.contrib.auth.setup_features.RegisterSelfConfirmMailFirstFeature()

            mail = balderhub.smtp.lib.setup_features.ProxySmtpReader(SmtpServer='SmtpServer')
            mail_confirm = MailConfirmationForRegistrationByLinkFeature()

This will execute the scenario with your setup:

.. code-block:: none

    +----------------------------------------------------------------------------------------------------------------------+
    | BALDER Testsystem                                                                                                    |
    |  python version 3.10.9 (main, Dec  8 2022, 02:19:14) [GCC 12.2.1 20220924] | balder version 0.2.2                    |
    +----------------------------------------------------------------------------------------------------------------------+
    Collect 1 Setups and 1 Scenarios
      resolve them to 1 valid variations

    ================================================== START TESTSESSION ===================================================
    SETUP SetupRegistrationRequestFirst
      SCENARIO ScenarioRegisterNewAsUnauth
        VARIATION ScenarioRegisterNewAsUnauth.Server:SetupRegistrationRequestFirst.Server | ScenarioRegisterNewAsUnauth.UnauthClient:SetupRegistrationRequestFirst.UnregisteredClient
          TEST ScenarioRegisterNewAsUnauth.test_register_new_user [.]
    ================================================== FINISH TESTSESSION ==================================================
    TOTAL NOT_RUN: 0 | TOTAL FAILURE: 0 | TOTAL ERROR: 0 | TOTAL SUCCESS: 1 | TOTAL SKIP: 0 | TOTAL COVERED_BY: 0


You need an implementation for the following features:

+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Property Name (From Example Setup) | Feature                                                                                            | Description                                             |
+====================================+====================================================================================================+=========================================================+
| ``role``                           | :class:`~balderhub.html.contrib.auth.scenario_features.ExtendedUserRole`                           | Config values for user (username, mail, password, ..)   |
|                                    |                                                                                                    | that should be used for registration (mail/username     |
|                                    |                                                                                                    | needs to be unused)                                     |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_req_register``              | :class:`~balderhub.html.contrib.auth.pages.RegistrationRequestPage`                                | Page Bindings for requesting the registration by        |
|                                    |                                                                                                    | confirming the mail address first                       |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``mail_confirm``                   | :class:`~balderhub.html.contrib.auth.setup_features.MailConfirmationForRegistrationByLinkFeature`  | Features provides constructions how the link can        |
|                                    |                                                                                                    | be extracted from mail / mail content is validated      |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_registration_finalize``     | :class:`~balderhub.html.contrib.auth.pages.RegistrationFinalizationPage`                           | Page Bindings for providing all other details of the    |
|                                    |                                                                                                    | user that is necessary for registration                 |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_registration_confirm``      | :class:`~balderhub.html.contrib.auth.pages.RegistrationConfirmationPage`                           | Page Bindings to the normal confirmation page after the |
|                                    |                                                                                                    | registration was successfully executed                  |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_login``                     | :class:`~balderhub.html.contrib.auth.pages.LoginPage`                                              | Page Bindings for the login page - necessary for        |
|                                    |                                                                                                    | validating if the registration was successful and user  |
|                                    |                                                                                                    | can log in afterwards                                   |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+

.. note::
    The scenario :class:`balderhub.auth.scenarios.ScenarioRegisterNewAsUnauth` does not provide a clean up fixture.
    Make sure, this is be handled within your setup fixtures.

Registration Processes (Mail First | Mail-Confirmation over Token)
------------------------------------------------------------------


.. list-table:: Process Register Request-First With Token
   :widths: 10 60 30
   :width: 100%
   :header-rows: 1
   :align: center

   * - **Step**
     - **Wireframe**
     - **Description**
   * - **1**
     - .. image:: /_static/RegistrationRequestPage.svg
           :align: center
           :alt: Wireframe of a Request-Registration Page, that expects the mail to be confirmed before providing more data for registration

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.RegistrationRequestPage`

     - Providing the mail address only
   * - **2**
     - .. image:: /_static/ReceiveMailToken.svg
           :align: center
           :alt: Symbol for waiting for a Mail with an activation link

       .. centered:: :class:`~balderhub.html.contrib.auth.setup_features.MailConfirmationForRegistrationByTokenFeature`

     - Waiting for a mail to the provided email address with a link to complete the registration
   * - **3**
     - .. image:: /_static/RegistrationInsertTokenPage.svg
           :align: center
           :alt: Wireframe of a Page, that expects the token received by mail after registration

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.RegistrationInsertTokenPage`

     - Confirmation Page, visible when the registration is completed
   * - **4**
     - .. image:: /_static/RegistrationFinalizationPage.svg
           :align: center
           :alt: Wireframe of the register finalization page, that will be presented when the user confirms the mail address

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.RegistrationFinalizationPage`

     - Finalization Page, visible when the mail is confirmed; form expects remaining registration data
   * - **5**
     - .. image:: /_static/RegistrationConfirmationPage.svg
           :align: center
           :alt: Wireframe of a widely used registration page

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.RegistrationConfirmationPage`

     - Confirmation Page, visible when the registration is completed

To test this workflow, you can use the :class:`balderhub.auth.scenarios.ScenarioRegisterNewAsUnauth`:


.. code-block:: python

    # file scenario_balderhub_auth.py

    from balderhub.auth.scenarios import ScenarioRegisterNewAsUnauth



For minimal required setup for the Request-First Registration process is shown below:

.. code-block:: python

    import balder
    import balder.connections as cnns

    import balderhub.html.contrib.auth.setup_features
    import balderhub.selenium.lib.setup_features
    import balderhub.smtp.lib.setup_features


    class SetupRegistrationRequestFirst(balder.Setup):
        class Server(balder.Device):
            pass

        class SmtpServer(balder.Device):
            smtp = balderhub.smtp.lib.setup_features.AiosmtpdServerFeature()

        @balder.connect(SmtpServer, over_connection=cnns.SmtpConnection)
        @balder.connect(Server, over_connection=balder.Connection)
        class UnregisteredClient(balder.Device):
            selenium = balderhub.selenium.lib.setup_features.SeleniumXXWebdriverFeature()  # or other feature that supports `balderhub-webdriver`

            role = UnregisteredUserRole()

            page_login = LoginPage()
            login = balderhub.html.contrib.auth.setup_features.UserLoginFeature()

            page_req_register = RegistrationRequestPage()
            page_register_insert_token = RegistrationInsertTokenPage()
            page_registration_finalize = RegistrationFinalizationPage()
            page_registration_confirm = RegistrationConfirmationPage()

            registration = balderhub.html.contrib.auth.setup_features.RegisterSelfConfirmMailFirstFeature()

            mail = balderhub.smtp.lib.setup_features.ProxySmtpReader(SmtpServer='SmtpServer')
            mail_confirm = MailConfirmationForRegistrationByTokenFeature()

This will execute the scenario with your setup:

.. code-block:: none

    +----------------------------------------------------------------------------------------------------------------------+
    | BALDER Testsystem                                                                                                    |
    |  python version 3.10.9 (main, Dec  8 2022, 02:19:14) [GCC 12.2.1 20220924] | balder version 0.2.2                    |
    +----------------------------------------------------------------------------------------------------------------------+
    Collect 1 Setups and 1 Scenarios
      resolve them to 1 valid variations

    ================================================== START TESTSESSION ===================================================
    SETUP SetupRegistrationRequestFirst
      SCENARIO ScenarioRegisterNewAsUnauth
        VARIATION ScenarioRegisterNewAsUnauth.Server:SetupRegistrationRequestFirst.Server | ScenarioRegisterNewAsUnauth.UnauthClient:SetupRegistrationRequestFirst.UnregisteredClient
          TEST ScenarioRegisterNewAsUnauth.test_register_new_user [.]
    ================================================== FINISH TESTSESSION ==================================================
    TOTAL NOT_RUN: 0 | TOTAL FAILURE: 0 | TOTAL ERROR: 0 | TOTAL SUCCESS: 1 | TOTAL SKIP: 0 | TOTAL COVERED_BY: 0


You need an implementation for the following features:

+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Property Name (From Example Setup) | Feature                                                                                            | Description                                             |
+====================================+====================================================================================================+=========================================================+
| ``role``                           | :class:`~balderhub.html.contrib.auth.scenario_features.ExtendedUserRole`                           | Config values for user (username, mail, password, ..)   |
|                                    |                                                                                                    | that should be used for registration (mail/username     |
|                                    |                                                                                                    | needs to be unused)                                     |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_req_register``              | :class:`~balderhub.html.contrib.auth.pages.RegistrationRequestPage`                                | Page Bindings for requesting the registration by        |
|                                    |                                                                                                    | confirming the mail address first                       |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``mail_confirm``                   | :class:`~balderhub.html.contrib.auth.setup_features.MailConfirmationForRegistrationByTokenFeature` | Features provides constructions how the token can       |
|                                    |                                                                                                    | be extracted from mail / mail content is validated      |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_register_insert_token``     | :class:`~balderhub.html.contrib.auth.pages.RegistrationInsertTokenPage`                            | Page Bindings, the token received by mail, needs to be  |
|                                    |                                                                                                    | inserted                                                |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_registration_finalize``     | :class:`~balderhub.html.contrib.auth.pages.RegistrationFinalizationPage`                           | Page Bindings for providing all other details of the    |
|                                    |                                                                                                    | user that is necessary for registration                 |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_registration_confirm``      | :class:`~balderhub.html.contrib.auth.pages.RegistrationConfirmationPage`                           | Page Bindings to the normal confirmation page after the |
|                                    |                                                                                                    | registration was successfully executed                  |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_login``                     | :class:`~balderhub.html.contrib.auth.pages.LoginPage`                                              | Page Bindings for the login page - necessary for        |
|                                    |                                                                                                    | validating if the registration was successful and user  |
|                                    |                                                                                                    | can log in afterwards                                   |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+

.. note::
    The scenario :class:`balderhub.auth.scenarios.ScenarioRegisterNewAsUnauth` does not provide a clean up fixture.
    Make sure, this is be handled within your setup fixtures.

Password Reset Processes | (Mail-Confirmation over Link)
--------------------------------------------------------

.. list-table:: Process Password-Reset With Link
   :widths: 10 60 30
   :width: 100%
   :header-rows: 1
   :align: center

   * - **Step**
     - **Wireframe**
     - **Description**
   * - **1**
     - .. image:: /_static/PasswordResetRequestPage.svg
           :align: center
           :alt: Wireframe of a password-reset request page, that triggers the password reset mail

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.PasswordResetRequestPage`

     - Providing the mail address and triggers the mail
   * - **2**
     - .. image:: /_static/ReceiveMailLink.svg
           :align: center
           :alt: Symbol for waiting for a Mail with an activation link

       .. centered:: :class:`~balderhub.html.contrib.auth.setup_features.MailConfirmationForPasswordResetByLinkFeature`

     - Waiting for a mail to the provided email address with a link for confirming mail access to reset password
   * - **3**
     - .. image:: /_static/PasswordResetFinalizationPage.svg
           :align: center
           :alt: Wireframe of a password-reset finalization Page, that will be presented when the user's mail was confirmed successfully

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.PasswordResetFinalizationPage`

     - Finalization Page, visible when the mail is confirmed; form asks for new password
   * - **4**
     - .. image:: /_static/PasswordResetConfirmationPage.svg
           :align: center
           :alt: Wireframe that shows the confirmation page, when password was changed successfully

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.PasswordResetConfirmationPage`

     - Confirmation Page, visible when the password reset has been completed and the password was changed

To test this workflow, you can use the :class:`balderhub.auth.scenarios.ScenarioPasswordResetWithUnauth`:


.. code-block:: python

    # file scenario_balderhub_auth.py

    from balderhub.auth.scenarios import ScenarioPasswordResetWithUnauth



For minimal required setup for the Password-Reset process is shown below:

.. code-block:: python

    import balder
    import balder.connections as cnns

    import balderhub.html.contrib.auth.setup_features
    import balderhub.selenium.lib.setup_features
    import balderhub.smtp.lib.setup_features


    class SetupPasswordReset(balder.Setup):
        class Server(balder.Device):
            pass

        class SmtpServer(balder.Device):
            smtp = balderhub.smtp.lib.setup_features.AiosmtpdServerFeature()

        @balder.connect(SmtpServer, over_connection=cnns.SmtpConnection)
        @balder.connect(Server, over_connection=balder.Connection)
        class Client(balder.Device):
            selenium = balderhub.selenium.lib.setup_features.SeleniumXXWebdriverFeature()  # or other feature that supports `balderhub-webdriver`

            role = MyUserRole()

            page_login = LoginPage()
            login = balderhub.html.contrib.auth.setup_features.UserLoginFeature()

            page_req_passwd_reset = PasswordResetRequestPage()
            page_finalize_passwd_reset = PasswordResetFinalizationPage()
            page_passwd_reset_confirm = PasswordResetConfirmationPage()

            passwd_provider = PasswordFieldValueProvider()
            passwd_reset = balderhub.html.contrib.auth.setup_features.PasswordResetFeature()

            mail = balderhub.smtp.lib.setup_features.ProxySmtpReader(SmtpServer='SmtpServer')
            mail_confirm = MailConfirmationForPasswdResetByLinkFeature()

This will execute the scenario with your setup:

.. code-block:: none

    +----------------------------------------------------------------------------------------------------------------------+
    | BALDER Testsystem                                                                                                    |
    |  python version 3.10.9 (main, Dec  8 2022, 02:19:14) [GCC 12.2.1 20220924] | balder version 0.1.0b1.dev461+ge459412d3|
    +----------------------------------------------------------------------------------------------------------------------+
    Collect 1 Setups and 1 Scenarios
      resolve them to 1 valid variations

    ================================================== START TESTSESSION ===================================================
    SETUP SetupPasswordReset
      SCENARIO ScenarioPasswordResetWithUnauth
        VARIATION ScenarioPasswordResetWithUnauth.Server:SetupPasswordReset.Server | ScenarioPasswordResetWithUnauth.UnauthClient:SetupPasswordReset.Client
          TEST ScenarioPasswordResetWithUnauth.test_password_reset [.]
    ================================================== FINISH TESTSESSION ==================================================
    TOTAL NOT_RUN: 0 | TOTAL FAILURE: 0 | TOTAL ERROR: 0 | TOTAL SUCCESS: 1 | TOTAL SKIP: 0 | TOTAL COVERED_BY: 0

You need an implementation for the following features:

+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Property Name (From Example Setup) | Feature                                                                                            | Description                                             |
+====================================+====================================================================================================+=========================================================+
| ``role``                           | :class:`~balderhub.html.contrib.auth.scenario_features.ExtendedUserRole`                           | Config values for user (username, mail, password, ..)   |
|                                    |                                                                                                    | the password should be changed for (user needs to       |
|                                    |                                                                                                    | exist)                                                  |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_req_passwd_reset``          | :class:`~balderhub.html.contrib.auth.pages.PasswordResetRequestPage`                               | Page Bindings for requesting the password-reset by      |
|                                    |                                                                                                    | confirming the mail address first                       |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``mail_confirm``                   | :class:`~balderhub.html.contrib.auth.setup_features.MailConfirmationForPasswdResetByLinkFeature`   | Features provides constructions how the link can        |
|                                    |                                                                                                    | be extracted from mail / mail content is validated      |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``passwd_provider``                | :class:`~balderhub.auth.lib.scenario_features.PasswordFieldValueProvider`                          | Features provides valid / invalid values for passwords  |
|                                    |                                                                                                    | where the primary valid value is used as new password   |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_finalize_passwd_reset``     | :class:`~balderhub.html.contrib.auth.pages.PasswordResetFinalizationPage`                          | Page Bindings to finalize the password reset, as soon   |
|                                    |                                                                                                    | as mail is confirmed and to provide new password        |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_passwd_reset_confirm``      | :class:`~balderhub.html.contrib.auth.pages.PasswordResetConfirmationPage`                          | Page Bindings to the normal confirmation page after the |
|                                    |                                                                                                    | password was changed successfully                       |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_login``                     | :class:`~balderhub.html.contrib.auth.pages.LoginPage`                                              | Page Bindings for the login page - necessary for        |
|                                    |                                                                                                    | validating if the password reset was done successfully  |
|                                    |                                                                                                    | and user can log in afterwards with the new password    |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+

Password Reset Processes | (Mail-Confirmation over Token)
---------------------------------------------------------

.. list-table:: Process Password-Reset With Token
   :widths: 10 60 30
   :width: 100%
   :header-rows: 1
   :align: center

   * - **Step**
     - **Wireframe**
     - **Description**
   * - **1**
     - .. image:: /_static/PasswordResetRequestPage.svg
           :align: center
           :alt: Wireframe of a password-reset request page, that triggers the password reset mail

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.PasswordResetRequestPage`

     - Providing the mail address only
   * - **2**
     - .. image:: /_static/ReceiveMailToken.svg
           :align: center
           :alt: Symbol for waiting for a Mail with an activation link

       .. centered:: :class:`~balderhub.html.contrib.auth.setup_features.MailConfirmationForPasswdResetByTokenFeature`

     - Waiting for a mail to the provided email address with a token for confirming mail access to reset password
   * - **3**
     - .. image:: /_static/PasswordResetInsertTokenPage.svg
           :align: center
           :alt: Wireframe of a Page, that expects the token received by mail after password-reset request

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.PasswordResetInsertTokenPage`

     - Page expecting to input the token that has been received by mail
   * - **4**
     - .. image:: /_static/PasswordResetFinalizationPage.svg
           :align: center
           :alt: Wireframe of a password-reset finalization Page, that will be presented when the user's mail was confirmed successfully

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.PasswordResetFinalizationPage`

     - Finalization Page, visible when the mail is confirmed; form asks for new password
   * - **5**
     - .. image:: /_static/PasswordResetConfirmationPage.svg
           :align: center
           :alt: Wireframe of the confirmation page, when the password-reset was successful

       .. centered:: :class:`~balderhub.html.contrib.auth.pages.PasswordResetConfirmationPage`

     - Confirmation Page, visible when the password-change has been completed and the new password was set

To test this workflow, you can use the :class:`balderhub.auth.scenarios.ScenarioPasswordResetWithUnauth`:


.. code-block:: python

    # file scenario_balderhub_auth.py

    from balderhub.auth.scenarios import ScenarioPasswordResetWithUnauth



For minimal required setup for the Password-Reset process is shown below:

.. code-block:: python

    import balder
    import balder.connections as cnns

    import balderhub.html.contrib.auth.setup_features
    import balderhub.selenium.lib.setup_features
    import balderhub.smtp.lib.setup_features


    class SetupPasswordReset(balder.Setup):
        class Server(balder.Device):
            pass

        class SmtpServer(balder.Device):
            smtp = balderhub.smtp.lib.setup_features.AiosmtpdServerFeature()

        @balder.connect(SmtpServer, over_connection=cnns.SmtpConnection)
        @balder.connect(Server, over_connection=balder.Connection)
        class Client(balder.Device):
            selenium = balderhub.selenium.lib.setup_features.SeleniumXXWebdriverFeature()  # or other feature that supports `balderhub-webdriver`

            role = MyUserRole()

            page_login = LoginPage()
            login = balderhub.html.contrib.auth.setup_features.UserLoginFeature()

            page_req_passwd_reset = PasswordResetRequestPage()
            page_token_passwd_reset = PasswordResetInsertTokenPage()
            page_finalize_passwd_reset = PasswordResetFinalizationPage()
            page_passwd_reset_confirm = PasswordResetConfirmationPage()

            passwd_provider = PasswordFieldValueProvider()
            passwd_reset = balderhub.html.contrib.auth.setup_features.PasswordResetFeature()

            mail = balderhub.smtp.lib.setup_features.ProxySmtpReader(SmtpServer='SmtpServer')
            mail_confirm = MailConfirmationForPasswdResetByLinkFeature()

This will execute the scenario with your setup:

.. code-block:: none

    +----------------------------------------------------------------------------------------------------------------------+
    | BALDER Testsystem                                                                                                    |
    |  python version 3.10.9 (main, Dec  8 2022, 02:19:14) [GCC 12.2.1 20220924] | balder version 0.1.0b1.dev461+ge459412d3|
    +----------------------------------------------------------------------------------------------------------------------+
    Collect 1 Setups and 1 Scenarios
      resolve them to 1 valid variations

    ================================================== START TESTSESSION ===================================================
    SETUP SetupPasswordReset
      SCENARIO ScenarioPasswordResetWithUnauth
        VARIATION ScenarioPasswordResetWithUnauth.Server:SetupPasswordReset.Server | ScenarioPasswordResetWithUnauth.UnauthClient:SetupPasswordReset.Client
          TEST ScenarioPasswordResetWithUnauth.test_password_reset [.]
    ================================================== FINISH TESTSESSION ==================================================
    TOTAL NOT_RUN: 0 | TOTAL FAILURE: 0 | TOTAL ERROR: 0 | TOTAL SUCCESS: 1 | TOTAL SKIP: 0 | TOTAL COVERED_BY: 0

You need an implementation for the following features:

+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Property Name (From Example Setup) | Feature                                                                                            | Description                                             |
+====================================+====================================================================================================+=========================================================+
| ``role``                           | :class:`~balderhub.html.contrib.auth.scenario_features.ExtendedUserRole`                           | Config values for user (username, mail, password, ..)   |
|                                    |                                                                                                    | the password should be changed for (user needs to       |
|                                    |                                                                                                    | exist)                                                  |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_req_passwd_reset``          | :class:`~balderhub.html.contrib.auth.pages.PasswordResetRequestPage`                               | Page Bindings for requesting the password-reset by      |
|                                    |                                                                                                    | confirming the mail address first                       |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_token_passwd_reset``        | :class:`~balderhub.html.contrib.auth.pages.PasswordResetInsertTokenPage`                           | Page Bindings, the token received by mail, needs to be  |
|                                    |                                                                                                    | inserted                                                |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``mail_confirm``                   | :class:`~balderhub.html.contrib.auth.setup_features.MailConfirmationForPasswdResetByTokenFeature`  | Features provides constructions how the link can        |
|                                    |                                                                                                    | be extracted from mail / mail content is validated      |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``passwd_provider``                | :class:`~balderhub.auth.lib.scenario_features.PasswordFieldValueProvider`                          | Features provides valid / invalid values for passwords  |
|                                    |                                                                                                    | where the primary valid value is used as new password   |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_finalize_passwd_reset``     | :class:`~balderhub.html.contrib.auth.pages.PasswordResetFinalizationPage`                          | Page Bindings to finalize the password reset, as soon   |
|                                    |                                                                                                    | as mail is confirmed and to provide new password        |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_passwd_reset_confirm``      | :class:`~balderhub.html.contrib.auth.pages.PasswordResetConfirmationPage`                          | Page Bindings to the normal confirmation page after the |
|                                    |                                                                                                    | password was changed successfully                       |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ``page_login``                     | :class:`~balderhub.html.contrib.auth.pages.LoginPage`                                              | Page Bindings for the login page - necessary for        |
|                                    |                                                                                                    | validating if the password reset was done successfully  |
|                                    |                                                                                                    | and user can log in afterwards with the new password    |
+------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------+

Pages
=====

Login / Logout Pages
--------------------

.. autoclass:: balderhub.html.contrib.auth.pages.LoginPage
    :members:

.. autoclass:: balderhub.html.contrib.auth.pages.LogoutPage
    :members:

Registration Pages
------------------

.. autoclass:: balderhub.html.contrib.auth.pages.RegistrationAllInOnePage
    :members:

.. autoclass:: balderhub.html.contrib.auth.pages.RegistrationRequestPage
    :members:

.. autoclass:: balderhub.html.contrib.auth.pages.RegistrationInsertTokenPage
    :members:

.. autoclass:: balderhub.html.contrib.auth.pages.RegistrationFinalizationPage
    :members:

.. autoclass:: balderhub.html.contrib.auth.pages.RegistrationConfirmationPage
    :members:


Password Reset Pages
--------------------

.. autoclass:: balderhub.html.contrib.auth.pages.PasswordResetRequestPage
    :members:

.. autoclass:: balderhub.html.contrib.auth.pages.PasswordResetInsertTokenPage
    :members:

.. autoclass:: balderhub.html.contrib.auth.pages.PasswordResetConfirmationPage
    :members:

Scenario Features
=================

This contrib module also provides some special scenario features that needs to be defined by end user.

Extended User Roles
-------------------

.. autoclass:: balderhub.html.contrib.auth.scenario_features.ExtendedUserRole
    :members:

Mail Extraction Features
------------------------

These features provide methods to extract information out of an email.

.. autoclass:: balderhub.html.contrib.auth.scenario_features.BaseMailExtractionFeature
    :members:

.. autoclass:: balderhub.html.contrib.auth.scenario_features.MailConfirmationForPasswdResetFeature
    :members:

.. autoclass:: balderhub.html.contrib.auth.scenario_features.MailConfirmationForRegistrationFeature
    :members:


Setup Features
==============

Login / Logout Setup Features
-----------------------------

.. autoclass:: balderhub.html.contrib.auth.setup_features.UserLoginFeature
    :members:

.. autoclass:: balderhub.html.contrib.auth.setup_features.UserLogoutFeature
    :members:

Registration Features
---------------------

.. autoclass:: balderhub.html.contrib.auth.setup_features.RegisterSelfAllDataAtOnceFeature
    :members:

.. autoclass:: balderhub.html.contrib.auth.setup_features.RegisterSelfConfirmMailFirstFeature
    :members:

Password Reset Setup-Level Features
-----------------------------------

.. autoclass:: balderhub.html.contrib.auth.setup_features.PasswordResetFeature
    :members:

Mail Confirmation Features
--------------------------

.. autoclass:: balderhub.html.contrib.auth.setup_features.MailConfirmationForPasswdResetByLinkFeature
    :members:

.. autoclass:: balderhub.html.contrib.auth.setup_features.MailConfirmationForPasswdResetByTokenFeature
    :members:

.. autoclass:: balderhub.html.contrib.auth.setup_features.MailConfirmationForRegistrationByLinkFeature
    :members:

.. autoclass:: balderhub.html.contrib.auth.setup_features.MailConfirmationForRegistrationByTokenFeature
    :members:
