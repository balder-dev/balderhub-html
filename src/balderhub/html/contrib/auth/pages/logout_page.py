from typing import Union, List

import balderhub.html.lib.scenario_features

from balderhub.url.lib.utils import Url


class LogoutPage(balderhub.html.lib.scenario_features.HtmlPage):
    """
    HTML Page for a normal logout
    """

    @property
    def url(self) -> Url:
        """
        :return: non-schema url the login page is located at
        """
        raise NotImplementedError

    @property
    def applicable_on_url_schema(self) -> Union[Url, List[Url]]:
        return self.url

    def open(self) -> None:
        """
        This method opens the login page.
        """
        self.driver.navigate_to(self.url)
