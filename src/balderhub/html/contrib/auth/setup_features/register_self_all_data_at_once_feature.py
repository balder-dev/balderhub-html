import logging

import balderhub.auth.lib.scenario_features.client
import balderhub.email.lib.scenario_features

from balderhub.html.contrib.auth.pages import RegistrationAllInOnePage, RegistrationConfirmationPage
from balderhub.html.contrib.auth.scenario_features import MailConfirmationForRegistrationFeature, ExtendedUserRole

logger = logging.getLogger(__name__)


class RegisterSelfAllDataAtOnceFeature(balderhub.auth.lib.scenario_features.client.RegisterSelfFeature):
    """
    Handles the registration process for a self-registration scenario where all data is provided at once.

    This class automates the process of self-registration by interacting with specific pages for requesting
    and confirming the registration, facilitating email confirmation, and ensuring the provided data aligns
    with the extended user role. It's designed to abstract and simplify the complex steps involved in this
    registration flow.
    """
    #: inner feature reference describing the role that defines the user's permissions and attributes for registration.
    role = ExtendedUserRole()

    #: inner feature reference to the page used to input registration data and initiate the registration process.
    request_link_page = RegistrationAllInOnePage()
    #: inner feature reference to the page\ displayed upon successful registration confirmation.
    confirmation_page = RegistrationConfirmationPage()

    #: inner feature reference, providing access to email handling features for reading and managing emails.
    mail = balderhub.email.lib.scenario_features.EmailReaderFeature()
    #: inner feature reference, providing access to email-based confirmation for the registration process.
    mail_confirm = MailConfirmationForRegistrationFeature()

    def register(self) -> None:
        mail_cnt_before = self.mail.total_mail_cnt

        self.request_link_page.open()
        self.request_link_page.fill_data_from_role()
        self.request_link_page.btn_submit.click()

        self.mail_confirm.confirm_with_mail_at_idx(mail_cnt_before)
        self.confirmation_page.wait_for_page()
