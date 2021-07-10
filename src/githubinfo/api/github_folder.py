class GitHubFolder:
    """
    This class is the main GitHub Folder.

    This class stands for a GitHub folder from a repository. This class doesn't
    have any data from the official GitHub API, but it stores files, which do.

    Attributes:
        name (str):
            The name of this folder
        parent (GitHubFolder):
            The parent folder (if the parent folder has a ``name`` attribute of
            ``/``, it is presumed that this folder is a top-level folder.)
        children (List[GitHubFolder, GitHubFile]):
            The children of this folder.
    """
    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        self.children = []
