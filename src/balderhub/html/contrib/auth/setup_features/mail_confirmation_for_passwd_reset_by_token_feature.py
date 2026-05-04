import logging

import balderhub.email.lib.utils
import balderhub.email.lib.scenario_features

from balderhub.html.contrib.auth.scenario_features import MailConfirmationForPasswdResetFeature
from balderhub.html.contrib.auth.pages import PasswordResetInsertTokenPage

logger = logging.getLogger(__name__)


class MailConfirmationForPasswdResetByTokenFeature(MailConfirmationForPasswdResetFeature):
    """
    Represents a feature for confirming password reset by token received via email.

    This class is used to implement functionality for extracting a token from an
    email and using it to confirm a password reset. It builds upon the base
    `MailConfirmationForPasswdResetFeature` and introduces token confirmation
    mechanisms.
    """
    #: inner feature reference to the inser-token page for password reset; used for token insertion and
    #: confirmation within the password reset process.
    page_token = PasswordResetInsertTokenPage()

    def extract_token(self, mail: balderhub.email.lib.utils.EmailDataMessage) -> str:
        """
        Extract a token from the given email message. The token is parsed from the
        email content and returned as a string.

        :param mail: The email message object from which the token is to be extracted.
                     This parameter must be an instance of EmailDataMessage.
        :return: The extracted token as a string.
        """
        raise NotImplementedError()

    def confirm_with_mail_at_idx(self, idx: int) -> None:
        self.mail.wait_for_min_total_mail_count_of(idx + 1)
        self.page_token.wait_for_page()

        mail = self.mail.get_mails()[idx]
        self.validate_mail(mail)
        token = self.extract_token(mail)

        logger.info(f'confirm password-reset by inserting token `{token}`')
        self.page_token.input_token.type_text(token, clean_before=True)
        self.page_token.btn_submit.click()
