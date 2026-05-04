import balderhub.auth.lib.scenario_features.client

from ..pages.logout_page import LogoutPage


class UserLogoutFeature(balderhub.auth.lib.scenario_features.client.UserLogoutFeature):
    """
    Provides functionality for user logout operation for web-based applications.

    This class is a feature implementation for handling the logout
    process of a user by interacting with the LogoutPage. It
    contains the necessary logic to complete the logout action.
    """
    #: dependent feature reference to `LogoutPage` instance that provides bindings to the logout page
    page_logout = LogoutPage()

    def logout(self) -> None:
        self.page_logout.open()
