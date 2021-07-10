from src.githubinfo.api.github_file import GitHubFile
from src.githubinfo.api.github_folder import GitHubFolder
from src.githubinfo.api.github_repo import GitHubRepo


class TestGitHubRepo:
    def setup_method(self):
        self.repo = GitHubRepo("Cutewarriorlover", "test-repo")
        folder = self.repo.root_folder
        folder.children.append(GitHubFile("file_1.txt", folder, "Hello 1!", "text"))
        folder.children.append(GitHubFile("file_2.txt", folder, "Hello 2!", "text"))
        folder.children.append(GitHubFile("file_3.txt", folder, "Hello 3!", "text"))
        folder.children.append(GitHubFile("file_4.txt", folder, "Hello 4!", "text"))
        folder.children.append(GitHubFile("file_5.txt", folder, "Hello 5!", "text"))
        folder.children.append(GitHubFile("file_6.txt", folder, "Hello 6!", "text"))

        new_folder = GitHubFolder(folder, "folder")
        folder.children.append(new_folder)

        new_folder.children.append(GitHubFile("file_1.txt", new_folder, "Hello 1!", "text"))
        new_folder.children.append(GitHubFile("file_2.txt", new_folder, "Hello 2!", "text"))
        new_folder.children.append(GitHubFile("file_3.txt", new_folder, "Hello 3!", "text"))
        new_folder.children.append(GitHubFile("file_4.txt", new_folder, "Hello 4!", "text"))
        new_folder.children.append(GitHubFile("file_5.txt", new_folder, "Hello 5!", "text"))
        new_folder.children.append(GitHubFile("file_6.txt", new_folder, "Hello 6!", "text"))

    def test_repo_dir(self):
        self.repo.root_folder.dir()


