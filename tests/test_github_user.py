from githubinfo.api.github_user import GitHubUser


class TestGitHubUser:
    def setup_method(self):
        self.user = GitHubUser("Cutewarriorlover")
