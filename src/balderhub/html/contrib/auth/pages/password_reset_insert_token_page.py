import balderhub.html.lib.scenario_features

import balderhub.html.lib.utils.components as html


class PasswordResetInsertTokenPage(balderhub.html.lib.scenario_features.HtmlPage):
    """
    HTML Page for ... todo

    .. image:: /_static/PasswordResetInsertTokenPage.svg
        :align: center
        :alt: Wireframe of a Page, that expects the token received by mail after password-reset request

    """


    @property
    def input_token(self) -> html.inputs.HtmlTextInput:
        """
        Provides the HTML Input element for the token.

        :return: HtmlTextInput instance representing the HTML element for the token.
        """
        raise NotImplementedError()

    @property
    def btn_submit(self) -> html.HtmlButtonElement:
        """
        Retrieves the HTML button element for submitting the page data.

        :return: The HTML button element for submitting the form.
        """
        raise NotImplementedError()
