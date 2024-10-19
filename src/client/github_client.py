import requests
import os

class GitHubClient:
    def __init__(self, token):
        self.base_url = "https://api.github.com"
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }

    def create_repo(self, repo_name, organization):
        url = f"{self.base_url}/orgs/{organization}/repos"
        data = {
            "name": repo_name,
            "private": True
        }
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()

    def create_issue(self, repo, title, body):
        url = f"{self.base_url}/repos/{repo}/issues"
        data = {"title": title, "body": body}
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()
