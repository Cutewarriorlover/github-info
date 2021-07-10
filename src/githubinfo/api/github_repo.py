from src.githubinfo.api.github_folder import GitHubFolder


class GitHubRepo:
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name
        self.rootFolder = GitHubFolder(None, "/")
    