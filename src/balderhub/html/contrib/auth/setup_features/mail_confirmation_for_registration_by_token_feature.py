import logging
import balderhub.email.lib.scenario_features
import balderhub.email.lib.utils

from balderhub.html.contrib.auth.scenario_features import MailConfirmationForRegistrationFeature
from balderhub.html.contrib.auth.pages import RegistrationInsertTokenPage

logger = logging.getLogger(__name__)


class MailConfirmationForRegistrationByTokenFeature(MailConfirmationForRegistrationFeature):
    """
    Provides functionality to confirm user registration by processing a confirmation token
    received via email. This feature interacts with the token insertion page and handles
    the extraction and usage of tokens for completing the registration process.
    """
    #: inner feature reference to the inner-token page for registration; used for token insertion and
    #: confirmation during user registration.
    page_token = RegistrationInsertTokenPage()

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

        logger.info(f'confirm registration by inserting token `{token}`')
        self.page_token.input_token.type_text(token, clean_before=True)
        self.page_token.btn_submit.click()
