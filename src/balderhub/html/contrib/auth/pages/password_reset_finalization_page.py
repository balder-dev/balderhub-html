import balderhub.html.lib.scenario_features

import balderhub.html.lib.utils.components as html


class PasswordResetFinalizationPage(balderhub.html.lib.scenario_features.HtmlPage):
    """
    HTML Page for finalize the password-reset by providing the new password.

    .. image:: _static/PasswordResetFinalizationPage.svg
        :align: center
        :alt: Wireframe of a password-reset finalization Page, that will be presented when the user's mail was confirmed
              successfully

    """

    @property
    def input_new_passwd(self) -> html.inputs.HtmlPasswordInput:
        """
        Gets the HTML input field for entering a new password.

        :return: HTML text input field for the new password.
        """
        raise NotImplementedError()

    @property
    def input_new_passwd_confirm(self) -> html.inputs.HtmlPasswordInput:
        """
        Retrieves the HTML text input element for confirming the new password.

        :return: The HTML text input component for confirming the new password.
        """
        raise NotImplementedError()

    @property
    def btn_submit(self) -> html.HtmlButtonElement:
        """
        Retrieves the HTML button element for submitting the page data.

        :return: The HTML button element for submitting the form.
        """
        raise NotImplementedError()
