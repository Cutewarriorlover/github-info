import json

import click
import requests

from src.githubinfo.api import GitHubUser

repo_link = "https://api.github.com/users/{}/repos"
auth = ("03d5bd8a8be4c06b556e", "2f11cef36b62e7a5c78debef50b96e895ada04b2")


@click.group()
def cli():
    pass


@click.command()
@click.argument("name")
def user(name):
    github_user = GitHubUser(name)
    click.echo(github_user)


@click.command()
@click.option("--user", help="User to get a list of repositories from")
def repos(user):
    contents = json.loads(requests.get(repo_link.format(user), auth=auth).content.decode("UTF-8"))

    print(f"{user}'s Public GitHub Repositories:\n")

    for repo in contents:
        string = f"""
{repo["full_name"]}:

For more information about this repository, you can use the following command:
    $ ghi repo {repo["name"]} --user {repo["owner"]["login"]}
""".strip()
        print(string)
        print("\n")


cli.add_command(user)
cli.add_command(repos)

if __name__ == '__main__':
    cli()
