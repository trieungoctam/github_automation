import os
from github import Github

def auto_grade(repo_name):
    g = Github(os.getenv("GITHUB_TOKEN"))
    repo = g.get_repo(repo_name)
    # GitHub Actions logic để kiểm tra code và unit tests
