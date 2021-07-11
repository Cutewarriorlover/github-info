"""
Main GitHub API Repository entry point.
"""
import json
import base64

import requests

from src.githubinfo.api.github_file import GitHubFile
from src.githubinfo.api.github_folder import GitHubRootFolder, GitHubFolder


class GitHubRepo:
    """
    Main GitHub API Repository.

    This class is the main GitHub API's repository. This represents a collection
    of files, along with metadata such as the repository's owner.
    """

    _api_repos_link = "https://api.github.com/repos/{}/{}"

    def __init__(self, owner, name):
        self.owner = owner
        self.name = name

        link = GitHubRepo._api_repos_link.format(self.owner, self.name)
        self.root_folder = GitHubRepo.get_file_structure(link)

    def __repr__(self):
        return f"""
Repository {self.owner}/{self.name}

File structure:
{self.root_folder.dir()}
""".strip()

    def get_url(self):
        """
        Returns the URL of this repository on GitHub.

        Returns:
            str:
                The GitHub repository URL.
        """
        return f"https://github.com/{self.owner}/{self.name}"

    @staticmethod
    def get_file_structure(url, parent_folder=GitHubRootFolder()):
        folder_name = [i for i in url.split("/")[7:] if i != ""]
        if folder_name:
            folder = GitHubFolder(parent_folder, "".join(folder_name).split("?")[0])
            parent_folder.children.append(folder)
        else:
            folder = parent_folder
        content_url = url + ("" if url.endswith("?ref=master") else "/contents")

        contents = json.loads(requests.get(content_url, auth=(
            "03d5bd8a8be4c06b556e", "2f11cef36b62e7a5c78debef50b96e895ada04b2")).content.decode("UTF-8"))

        for item in contents:
            if item["type"] == "dir":
                GitHubRepo._recurse_get_folders(item["git_url"], folder)

        for item in contents:
            name = item["name"]
            html_url = item["html_url"]
            if item["type"] == "file":
                raw_url = item["download_url"]
                try:
                    contents = requests.get(raw_url, auth=(
                        "03d5bd8a8be4c06b556e", "2f11cef36b62e7a5c78debef50b96e895ada04b2")).content.decode("UTF-8")
                except UnicodeDecodeError:
                    contents = "ERROR"

                file_object = GitHubFile(name, parent_folder, contents, "." + name.split(".")[-1])

                folder.children.append(file_object)

        return parent_folder

    @staticmethod
    def _recurse_get_folders(git_url, parent_folder):
        git_url += "?recursive=true"

        auth = ("03d5bd8a8be4c06b556e", "2f11cef36b62e7a5c78debef50b96e895ada04b2")
        contents = json.loads(requests.get(git_url, auth=auth).content.decode("UTF-8"))

        for file in contents["tree"]:
            root_path = "".join(file["path"].split("/")[:-1])
            parent = parent_folder.get_file_from_path(root_path)

            name = "".join(file["path"].split("/"))

            if file["type"] == "blob":
                contents = json.loads(requests.get(file["url"], auth=auth).content.decode("UTF-8"))
                contents = base64.b64decode(contents["content"])
                parent.children.append(GitHubFile(name, parent, contents, name.split(".")[-1]))
            elif file["type"] == "tree":
                parent.children.append(GitHubFolder(parent, name))
