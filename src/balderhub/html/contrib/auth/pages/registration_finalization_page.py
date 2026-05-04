
import balderhub.html.lib.scenario_features

import balderhub.html.lib.utils.components as html

from ..scenario_features.extended_user_role import ExtendedUserRole


class RegistrationFinalizationPage(balderhub.html.lib.scenario_features.HtmlPage):
    """
    HTML Page for finalize the registration process for a new user with data provided by
    :class:`balderhub.html.contrib.auth.scenario_features.ExtendedUserRole` that is assigned to the same device.

    This page will be opened after successfully confirm the mail address when the register-with-request-process

    .. image:: /_static/RegistrationFinalizationPage.svg
        :align: center
        :alt: Wireframe of the register finalization page, that will be presented when the user confirms the mail
              address


    """
    role = ExtendedUserRole()


    @property
    def input_passwd(self) -> html.inputs.HtmlPasswordInput:
        """
        Provides the HTML Input element for the password

        :return: HtmlTextInput instance representing the HTML element for the password.
        """
        raise NotImplementedError

    @property
    def input_passwd_confirm(self) -> html.inputs.HtmlPasswordInput:
        """
        Provides the HTML Input element for confirming the password

        :return: HtmlTextInput instance representing the HTML element for confirming the password.
        """
        raise NotImplementedError

    @property
    def btn_submit(self) -> html.HtmlButtonElement:
        """
        Retrieves the HTML button element for submitting the page data.

        :return: The HTML button element for submitting the form.
        """
        raise NotImplementedError

    def fill_data_from_role(self):
        """
        Method that fills the data based on the given role. Needs to be overwritten if there are more fields that
        are necessary to fill in.
        """
        self.input_passwd.type_text(self.role.password, clean_before=True)
        self.input_passwd_confirm.type_text(self.role.password, clean_before=True)
