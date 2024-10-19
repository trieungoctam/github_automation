import requests

def track_student_progress(github_client, repo_name):
    url = f"https://api.github.com/repos/{repo_name}/commits"
    commits = requests.get(url, headers=github_client.headers).json()
    return len(commits)
