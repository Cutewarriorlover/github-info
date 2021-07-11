"""
Main entry point to the GitHub file.
"""


class GitHubFile:
    """
    This is the main GitHub File.

    This class stands for a main GitHub file. This class's doesn't directly get
    data from the GitHub API.

    Attributes:
        name (str):
            This name of this file.
        parent (GitHubFolder | GitHubRootFolder):
            The parent folder (if the parent folder has type of :class:`GitHubRootFolder`,
            it is presumed this folder is a top level folder.)
        contents (str):
            The contents of this file.
        extension (str):
            Extension of this file.
    """

    def __init__(self, name, parent, contents, extension):
        self.name = name
        self.parent = parent
        self.contents = contents
        self.extension = extension

    def __repr__(self):
        return f"{self.name}"

    def syntax_ansi(self):
        """
        Returns the contents of this file with syntax highlighting in the ANSI
        format.

        Returns:
            str:
                The contents of this file with syntax highlighting in the ANSI format.
        """
        raise NotImplementedError()
