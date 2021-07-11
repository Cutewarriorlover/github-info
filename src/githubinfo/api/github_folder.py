"""
Main entry point of the GitHub API's Folder.
"""

from src.githubinfo.api.github_file import GitHubFile


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

    def dir(self, nesting=1):
        result = ""
        indent = nesting * "    "

        for item in self.children:
            if isinstance(item, GitHubFolder):
                result += item.dir(nesting + 1)
            elif isinstance(item, GitHubFile):
                result += "\n"
                result += indent + "├── " + item.name
            return result

    def get_file_from_path(self, path):
        split_path = [i for i in path.split("/") if i != ""]
        
        if len(split_path) == 0:
            return self

        for item in self.children:
            if item.name == split_path[0]:
                if len(split_path) == 1:
                    return item
                else:
                    return self.get_file_from_path("".join(split_path[1:]))
                
        raise ValueError("Cannot find item with name '{}'".format(split_path[0]))


class GitHubRootFolder(GitHubFolder):
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

    def dir(self, nesting=0):
        result = ""

        for item in self.children:
            result += "\n"
            if isinstance(item, GitHubFolder):
                result += "├── " + item.name + "/"
                result += item.dir()
            if isinstance(item, GitHubFile):
                result += "├── " + item.name

        return result
