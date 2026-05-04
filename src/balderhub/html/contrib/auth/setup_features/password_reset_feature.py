import logging

import balderhub.auth.lib.scenario_features.client
import balderhub.email.lib.scenario_features


from balderhub.html.contrib.auth.pages import PasswordResetRequestPage, PasswordResetFinalizationPage, \
    PasswordResetConfirmationPage
from balderhub.html.contrib.auth.scenario_features import ExtendedUserRole, MailConfirmationForPasswdResetFeature

logger = logging.getLogger(__name__)


class PasswordResetFeature(balderhub.auth.lib.scenario_features.client.PasswordResetFeature):
    """
    Handles the password reset process for a user within a web-based application.

    This class orchestrates the password reset procedure by initiating the reset request,
    confirming the reset through an email verification step, and allowing the user to
    set a new password. It relies on multiple pages and feature classes to facilitate
    the process and interacts with email confirmation functionality.
    """
    #: dependent feature, represents the user role associated with the password reset process.
    role = ExtendedUserRole()

    #: dependent feature, represents the page for initiating the password reset request.
    page_reset_req = PasswordResetRequestPage()
    #: dependent feature, represents the page for finalizing the password reset process.
    page_reset_finalize = PasswordResetFinalizationPage()
    #: dependent feature, represents the page for confirming the password has been reset.
    page_reset_confirm = PasswordResetConfirmationPage()

    #: dependent feature, handles email interactions, such as retrieving the confirmation email.
    mail = balderhub.email.lib.scenario_features.EmailReaderFeature()
    #: dependent feature, facilitates email confirmation for the password reset process.
    mail_confirm = MailConfirmationForPasswdResetFeature()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._mail_cnt_before = None

    def initiate_reset(self):

        self.page_reset_req.open()
        self.page_reset_req.wait_for_page()

        self._mail_cnt_before = self.mail.total_mail_cnt
        self.page_reset_req.input_email.wait_to_be_clickable_for(2).type_text(self.role.email)
        self.page_reset_req.btn_submit.click()

    def confirm_over_second_factor(self):
        self.mail_confirm.confirm_with_mail_at_idx(self._mail_cnt_before)

    def change_password(self, new_password: str):
        self.page_reset_finalize.wait_for_page()

        self.page_reset_finalize.input_new_passwd.type_text(new_password)
        self.page_reset_finalize.input_new_passwd_confirm.type_text(new_password)
        self.page_reset_finalize.btn_submit.click()

        self.page_reset_confirm.wait_for_page()
