from typing import Union, List

from balderhub.url.lib.utils import Url

import balderhub.html.lib.scenario_features


class PasswordResetConfirmationPage(balderhub.html.lib.scenario_features.HtmlPage):
    """
    HTML Page for ... todo

    .. image:: /_static/PasswordResetConfirmationPage.svg
        :align: center
        :alt: Wireframe of the confirmation page, when the password-reset was successful

    """

    @property
    def applicable_on_url_schema(self) -> Union[Url, List[Url]]:
        raise NotImplementedError
