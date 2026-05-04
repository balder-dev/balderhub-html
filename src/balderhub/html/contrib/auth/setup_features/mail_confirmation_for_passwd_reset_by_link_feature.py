import logging
import balderhub.email.lib.utils
import balderhub.email.lib.scenario_features
from balderhub.url.lib.utils import Url
import balderhub.webdriver.lib.scenario_features

from balderhub.html.contrib.auth.scenario_features import MailConfirmationForPasswdResetFeature

logger = logging.getLogger(__name__)


class MailConfirmationForPasswdResetByLinkFeature(MailConfirmationForPasswdResetFeature):
    """
    Provides functionality for mail-based password reset confirmation using a link.

    This class extends `MailConfirmationForPasswdResetFeature` and is designed to handle
    the confirmation of password reset processes via email by parsing and extracting
    reset links from received messages. It uses a webdriver to navigate to the reset links
    for confirmation.
    """
    #: inner feature reference to the webdriver feature for controlling browser interactions during the password
    #: reset confirmation process.
    webdriver = balderhub.webdriver.lib.scenario_features.WebdriverControlFeature()

    def extract_link(self, mail: balderhub.email.lib.utils.EmailDataMessage) -> Url:
        """
        Extracts a URL from a given email message.

        This method is designed to locate and return the password-reset confirmation URL present in the provided
        email message.

        :param mail: The email message object from which the URL is to be extracted.
            The object should be compatible with the EmailDataMessage class.
        :return: The extracted URL from the email message as :class:`balderhub.url.lib.utils.Url` object.
        """
        raise NotImplementedError()

    def confirm_with_mail_at_idx(self, idx: int) -> None:

        self.mail.wait_for_min_total_mail_count_of(idx + 1)

        mail = self.mail.get_mails()[idx]
        self.validate_mail(mail)
        link = self.extract_link(mail)

        logger.info(f'confirm password-reset by opening `{link}`')
        self.webdriver.driver.navigate_to(link)
