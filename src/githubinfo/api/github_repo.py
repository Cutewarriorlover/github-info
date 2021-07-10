from src.githubinfo.api.github_folder import GitHubRootFolder


class GitHubRepo:
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name
        self.root_folder = GitHubRootFolder()
