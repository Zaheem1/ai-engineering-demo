import os

from dotenv import load_dotenv
from github import Github

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")
repo_name = os.getenv("GITHUB_REPO")

github = Github(github_token)

repo = github.get_repo(repo_name)


def get_pull_request(pr_number):
    pr = repo.get_pull(pr_number)

    return {
        "number": pr.number,
        "title": pr.title,
        "description": pr.body or "",
        "author": pr.user.login,
    }


if __name__ == "__main__":
    pr = get_pull_request(1)

    print("Pull Request:")
    print(pr)