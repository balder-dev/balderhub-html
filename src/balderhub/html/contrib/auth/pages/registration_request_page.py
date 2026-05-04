from typing import Union, List

import balderhub.html.lib.scenario_features

import balderhub.html.lib.utils.components as html
from balderhub.url.lib.utils import Url


class RegistrationRequestPage(balderhub.html.lib.scenario_features.HtmlPage):
    """
    HTML Page for ... todo

    .. image:: /_static/RegistrationRequestPage.svg
        :align: center
        :alt: Wireframe of a Request-Registration Page, that expects the mail to be confirmed before providing more data
              for registration

    """

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
    def btn_submit(self) -> html.HtmlButtonElement:
        """
        Retrieves the HTML button element for submitting the page data.

        :return: The HTML button element for submitting the form.
        """
        raise NotImplementedError
