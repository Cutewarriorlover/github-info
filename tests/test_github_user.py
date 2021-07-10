from githubinfo.api import GitHubUser


class TestGitHubUser:
    def setup_method(self):
        self.user = GitHubUser("Cutewarriorlover")
        
    def test_user_profile_url(self):
        assert self.user.github_url() == "https://github.com/Cutewarriorlover"
        
    def test_user_repr(self):
        print(self.user)
