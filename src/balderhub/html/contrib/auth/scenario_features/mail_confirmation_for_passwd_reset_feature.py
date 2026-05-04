import balderhub.email.lib.utils

from .base_mail_extraction_feature import BaseMailExtractionFeature


class MailConfirmationForPasswdResetFeature(BaseMailExtractionFeature):
    """
    Handles the mail-based confirmation process for password-reset requests.

    This feature provides the functionality to confirm password-reset requests by processing
    incoming emails. This class must be extended to implement the specific logic
    for email validation and processing the mail-confirmation necessary when a user forgets his/her password.
    """

    def confirm_with_mail_at_idx(self, idx: int) -> None:
        """
        Executes the full process that is necessary to confirm the password-reset request by reading the mail at the
        given index.

        This method is responsible for validating the mail and executing the process that is
        necessary to provide the confirmation with the new information given within the mail at the given index.

        :param idx: the mail index of all received emails by the dependent
                    :class:`balderhub.email.lib.scenario_features.EmailReaderFeature`
        """
        raise NotImplementedError()

    def validate_mail(self, mail: balderhub.email.lib.utils.EmailDataMessage):
        """
        Validates the given email message.

        This method ensures that the provided email message adheres to the mail format expected for
        a password-reset request. It must be implemented by subclasses to define the validation logic.

        :param mail: An instance of EmailDataMessage that represents the email to be validated.
        """
        raise NotImplementedError()
