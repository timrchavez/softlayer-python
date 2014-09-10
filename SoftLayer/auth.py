"""
    SoftLayer.auth
    ~~~~~~~~~~~~~~
    Module with the supported auth mechanisms for the SoftLayer API

    :license: MIT, see LICENSE for more details.
"""
__all__ = ['BasicAuthentication', 'TokenAuthentication', 'AuthenticationBase']


class AuthenticationBase(object):
    """A base authentication class intended to be overridden."""
    def get_options(self, options):
        """Receives request options and returns request options."""
        raise NotImplementedError


class TokenAuthentication(AuthenticationBase):
    """Token-based authentication class.

        :param user_id int: a user's id
        :param auth_token str: a user's auth token, attained through
                               User_Customer::getPortalLoginToken
    """
    def __init__(self, user_id, auth_token):
        self.user_id = user_id
        self.auth_token = auth_token

    def get_options(self, options):
        """Sets token-based auth headers."""
        options['headers']['authenticate'] = {
            'complexType': 'PortalLoginToken',
            'userId': self.user_id,
            'authToken': self.auth_token,
        }
        return options

    def __repr__(self):
        return "<TokenAuthentication: %s %s>" % (self.user_id, self.auth_token)


class BasicAuthentication(AuthenticationBase):
    """Token-based authentication class.

        :param username str: a user's username
        :param api_key str: a user's API key
    """
    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key

    def get_options(self, options):
        """Sets token-based auth headers."""
        options['headers']['authenticate'] = {
            'username': self.username,
            'apiKey': self.api_key,
        }
        return options

    def __repr__(self):
        return "<BasicAuthentication: %s>" % (self.username)
