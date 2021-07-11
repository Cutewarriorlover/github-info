"""
This module contains the main GitHub User class.

While the user's information can be updated, to update :class:`GitHubUser`'s
information, you need to call the :meth:`GitHubUser.update` method.
"""

import requests
import json
from dateutil import parser
from datetime import datetime

from src.githubinfo.api.github_repo import GitHubRepo


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
        self.username = self.data["login"]  # Username is case-insensitive
        self.repos = []

        repos = json.loads(requests.get(self.data["repos_url"]).content.decode("UTF-8"))

        for repo in repos:
            self.repos.append(GitHubRepo(self.username, repo["name"]))

    def __repr__(self):
        return f"""
Info about user {self.data["login"]}
Avatar image: {self.data["avatar_url"]}

User home page: {self.data["html_url"]}

User join time: {self.join_time}

Commands:
    To get a list of this user's repositories, use the following command:
        $ ghi repos --user {self.data["login"]}

    To get a list of this user's GitHub Gists, use the following command:
        $ ghi gists --user {self.data["login"]}

    To get a list of this user's followers, use the following command:
        $ ghi followers --user {self.data["login"]}

    To get a list of the users this user is following, use the following command:
        $ ghi following --user {self.data["login"]}

    To get a list of the repositories this user has starred, use the following command:
        $ ghi starred --user {self.data["login"]}
""".strip()

    def update(self):
        """
        Updates the user's data.

        This method gives a ``GET`` request to the GitHub API, updating its
        information.

        .. Caution::
            While this method is guaranteed to retrieve the user's information,
            it is possible that GitHub's API hasn't updated yet.
        """
        self.data = requests.get(f"https://api.github.com/users/{self.username}", auth=("03d5bd8a8be4c06b556e", "2f11cef36b62e7a5c78debef50b96e895ada04b2"))

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

    def join_time(self):
        join_time = parser.parse(self.data["created_at"])
        join_time = float(join_time.strftime("%s"))
        join_time = datetime.fromtimestamp(join_time)
        join_time = join_time.strftime("%A, %B %d, %Y at %I:%M %p")

        return join_time
