from typing import Union, List

import balderhub.html.lib.scenario_features

import balderhub.html.lib.utils.components as html
from balderhub.url.lib.utils import Url

from ..scenario_features.extended_user_role import ExtendedUserRole


class RegistrationAllInOnePage(balderhub.html.lib.scenario_features.HtmlPage):
    """
    HTML Page for register a new user with data provided by
    :class:`balderhub.html.contrib.auth.scenario_features.ExtendedUserRole` that is assigned to the same device.

    .. image:: /_static/RegistrationAllInOnePage.svg
        :align: center
        :alt: Wireframe of a widely used registration page

    """
    role = ExtendedUserRole()

    @property
    def url(self) -> Url:
        """
        :return: non-schema url the page is located at
        """
        raise NotImplementedError

    @property
    def applicable_on_url_schema(self) -> Union[Url, List[Url]]:
        return self.url

    def open(self) -> None:
        """
        This method opens the page.
        """
        self.driver.navigate_to(self.url)

    @property
    def input_email(self) -> html.inputs.HtmlEmailInput:
        """
        Provides the HTML Input element for the email address.

        :return: HtmlTextInput instance representing the HTML element for the email address.
        """
        raise NotImplementedError

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

    def fill_data_from_role(self) -> None:
        """
        Method that fills the data based on the given role. Needs to be overwritten if there are more fields that
        are necessary to fill in.
        """
        self.input_email.type_text(self.role.email, clean_before=True)
        self.input_passwd.type_text(self.role.password, clean_before=True)
        self.input_passwd_confirm.type_text(self.role.password, clean_before=True)
