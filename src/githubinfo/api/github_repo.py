"""
Main GitHub API Repository entry point.
"""


from src.githubinfo.api.github_folder import GitHubRootFolder


class GitHubRepo:
    """
    Main GitHub API Repository.

    This class is the main GitHub API's repository. This represents a collection
    of files, along with metadata such as the repository's owner.
    """
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name
        self.root_folder = GitHubRootFolder()

    def __repr__(self):
        return f"""
Repository {self.owner}/{self.name}

File structure:
{self.root_folder}
""".strip()

    def get_url(self):
        """
        Returns the URL of this repository on GitHub.

        Returns:
            str:
                The GitHub repository URL.
        """
        return f"https://github.com/{self.owner}/{self.name}"
