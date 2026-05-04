import balder
import balderhub.email.lib.utils
import balderhub.email.lib.scenario_features

class BaseMailExtractionFeature(balder.Feature):
    """
    A base feature class for mail extraction for this contribution project.

    This class provides scenario-level functionalities related  to mail extraction involving email handling.

    """
    #: Instance of the email reader feature
    mail = balderhub.email.lib.scenario_features.EmailReaderFeature()

    def confirm_with_mail_at_idx(self, idx: int) -> None:
        """
        Executes the full process that is necessary to confirm the expected use by reading the mail at the given index.

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
        the current process type. It must be implemented by subclasses to define the validation logic.

        :param mail: An instance of EmailDataMessage that represents the email to be validated.
        """
        raise NotImplementedError()
