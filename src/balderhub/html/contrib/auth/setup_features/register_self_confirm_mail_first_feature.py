import logging

import balderhub.auth.lib.scenario_features.client
import balderhub.email.lib.scenario_features

from balderhub.html.contrib.auth.pages import RegistrationRequestPage, RegistrationFinalizationPage, \
    RegistrationConfirmationPage
from balderhub.html.contrib.auth.scenario_features import MailConfirmationForRegistrationFeature, ExtendedUserRole

logger = logging.getLogger(__name__)


class RegisterSelfConfirmMailFirstFeature(balderhub.auth.lib.scenario_features.client.RegisterSelfFeature):
    """
    Handles the registration flow for a user, starting with requesting a registration
    confirmation link, processing the confirmation email, and finalizing the registration.

    This class is designed to automate the self-registration process for a specific type
    of user and includes interaction with multiple pages involved in the workflow,
    as well as handling email confirmation for registration completion.

    :ivar role: Represents the role of the user being registered, containing details
        like email and other relevant user information.
    :type role: ExtendedUserRole
    :ivar request_link_page: Manages the interaction with the registration request page,
        where users input their email address for registration.
    :type request_link_page: RegistrationRequestPage
    :ivar registration_page: Handles the final registration form page where users
        provide additional details to complete their registration.
    :type registration_page: RegistrationFinalizationPage
    :ivar confirmation_page: Represents the page displayed post successful
        registration confirmation.
    :type confirmation_page: RegistrationConfirmationPage
    :ivar mail: Handles interaction with the email system, such as checking for
        registration messages.
    :type mail: EmailReaderFeature
    :ivar mail_confirm: Provides functionality to process and verify registration
        links received via email.
    :type mail_confirm: MailConfirmationForRegistrationFeature
    """

    #: inner feature reference describing the role that defines the user's permissions and attributes for registration.
    role = ExtendedUserRole()

    #: inner feature reference to the page used to input the email address and initiate the registration process.
    request_link_page = RegistrationRequestPage()
    #: inner feature reference to the page used to finalize the registration by providing all missing data
    registration_page = RegistrationFinalizationPage()
    #: inner feature reference to the page displayed upon successful registration confirmation.
    confirmation_page = RegistrationConfirmationPage()

    #: inner feature reference, providing access to email handling features for reading and managing emails.
    mail = balderhub.email.lib.scenario_features.EmailReaderFeature()
    #: inner feature reference, providing access to email-based confirmation for the registration process.
    mail_confirm = MailConfirmationForRegistrationFeature()

    def register(self) -> None:
        mail_cnt_before = self.mail.total_mail_cnt

        self.request_link_page.open()
        self.request_link_page.input_email.type_text(self.role.email)
        self.request_link_page.btn_submit.click()

        self.mail_confirm.confirm_with_mail_at_idx(mail_cnt_before)
        self.registration_page.wait_for_page()

        self.registration_page.fill_data_from_role()
        self.registration_page.btn_submit.click()

        self.confirmation_page.wait_for_page()
