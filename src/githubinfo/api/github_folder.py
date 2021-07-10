"""
Main entry point of the GitHub API's Folder.
"""

from src.githubinfo.api.github_file import GitHubFile


class GitHubRootFolder:
    """
    This class is a repository's root folder.

    A repository's root folder is the folder that you see when you navigate to
    the repository's link. It has no parent.

    Attributes:
        name (str):
            The name of this folder. This should *always* be ``/``.
        children (List[GitHubFolder, GitHubFile]):
            The children of this folder.
    """

    def __init__(self):
        self.name = "/"
        self.children = []

    def __repr__(self):
        result = ""

        for item in self.children:
            if isinstance(item, GitHubFolder):
                result += (item.name + "/")
                result += repr(item)
            elif isinstance(item, GitHubFile):
                result += item.name

        return result


class GitHubFolder:
    """
    This class is the main GitHub Folder.

    This class stands for a GitHub folder from a repository. This class doesn't
    have any data from the official GitHub API, but it stores files, which do.

    Attributes:
        name (str):
            The name of this folder.
        parent (GitHubFolder | GitHubRootFolder):
            The parent folder (if the parent folder has type of :class:`GitHubRootFolder`,
            it is presumed this folder is a top level folder.)
        children (List[GitHubFolder, GitHubFile]):
            The children of this folder.
    """

    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        self.children = []

    def __repr__(self, nesting=1):
        result = ""
        indent = nesting * "    "

        for item in self.children:
            if isinstance(item, GitHubFolder):
                result += repr(nesting + 1)
            elif isinstance(item, GitHubFile):
                result += indent + item.name

        return result
