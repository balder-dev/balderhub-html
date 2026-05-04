import balderhub.auth.lib.scenario_features.client.role


class ExtendedUserRole(balderhub.auth.lib.scenario_features.client.role.UserRoleFeature):
    """
    Represents an extended user role with additional properties, necessary for web-based authentification.
    """
    @property
    def email(self) -> str:
        """
        :return: represents the email address associated with the user role.
        """
        raise NotImplementedError
