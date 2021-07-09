import requests


class GitHubUser:
    def __init__(self, username):
        self.data = requests.get(f"https://api.github.com/users/{username}").json()
