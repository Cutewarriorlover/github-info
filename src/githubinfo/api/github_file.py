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
        type_ (str):
            The type of this file. This should be in lowercase. For example:

            - python
            - javascript
            - java
            - markdown

            This format shouldn't be in abbreviation form. The following counts
            as abbreviation:

            - py
            - js
            - md

            While those may be used commonly, they shouldn't be used here.
    """
    def __init__(self, name, parent, contents, type_):
        self.name = name
        self.parent = parent
        self.contents = contents
        self.type_ = type_
