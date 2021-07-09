"""
This module contains the main GitHub User class.

While the user's information can be updated, to update :class:`GitHubUser`'s
information, you need to call the :meth:`GitHubUser.update` method.
"""

import requests


class GitHubUser:
    """
    This class is the main GitHub user.

    This class stands for a single GitHub user. It gets its data from the
    official GitHub API (using the link ``https://api.github.com/users/{username}``,
    where ``{username}`` is the username of the owner of the data.

    Attributes:
        username (str):
            The username of the owner of this account.
    """

    def __init__(self, username):
        self.username = username
        self.data = requests.get(f"https://api.github.com/users/{username}").json()

    def update(self):
        """
        Updates the user's data.

        This method gives a ``GET`` request to the GitHub API, updating its
        information.

        .. Caution::
            While this method is guaranteed to retrieve the user's information,
            it is possible that GitHub's API hasn't updated yet.
        """
        self.data = requests.get(f"https://api.github.com/users/{self.username}")

    def github_url(self):
        """
        Gives the user's GitHub profile link.

        This method return the user's GitHub profile link. This link is where
        the user will land if the user is in the web.

        .. Important::
            This link should *always* start with ``https://github.com/``. If
            this is not true, **don't click on the link**! Please send a GitHub
            issue at https://github.com/Cutewarriorlover/github-info/issues
            if it ever happens.

        Returns:
            str: The link to the user's GitHub profile.
        """
        return self.data["html_url"]
