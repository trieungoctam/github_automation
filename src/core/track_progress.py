import requests
from datetime import datetime, timedelta

def track_student_progress(github_client, repo_name, days=30):
    progress = {
        'commits': get_commits(github_client, repo_name, days),
        'pull_requests': get_pull_requests(github_client, repo_name, days),
        'issues': get_issues(github_client, repo_name, days)
    }
    
    summary = summarize_progress(progress)
    return progress, summary

def get_commits(github_client, repo_name, days):
    url = f"{github_client.base_url}/repos/{repo_name}/commits"
    params = {'since': (datetime.now() - timedelta(days=days)).isoformat()}
    response = github_client.get(url, params=params)
    commits = response.json()
    return [{'sha': commit['sha'], 'date': commit['commit']['author']['date'], 
             'message': commit['commit']['message']} for commit in commits]

def get_pull_requests(github_client, repo_name, days):
    url = f"{github_client.base_url}/repos/{repo_name}/pulls"
    params = {'state': 'all'}
    response = github_client.get(url, params=params)
    prs = response.json()
    return [{'number': pr['number'], 'title': pr['title'], 'state': pr['state'], 
             'created_at': pr['created_at'], 'closed_at': pr['closed_at']} 
            for pr in prs if pr_within_days(pr, days)]

def get_issues(github_client, repo_name, days):
    url = f"{github_client.base_url}/repos/{repo_name}/issues"
    params = {'state': 'all'}
    response = github_client.get(url, params=params)
    issues = response.json()
    return [{'number': issue['number'], 'title': issue['title'], 'state': issue['state'], 
             'created_at': issue['created_at'], 'closed_at': issue['closed_at']} 
            for issue in issues if issue_within_days(issue, days)]

def pr_within_days(pr, days):
    created_at = datetime.strptime(pr['created_at'], "%Y-%m-%dT%H:%M:%SZ")
    return (datetime.now() - created_at).days <= days

def issue_within_days(issue, days):
    created_at = datetime.strptime(issue['created_at'], "%Y-%m-%dT%H:%M:%SZ")
    return (datetime.now() - created_at).days <= days

def summarize_progress(progress):
    summary = {
        'total_commits': len(progress['commits']),
        'total_prs': len(progress['pull_requests']),
        'open_prs': sum(1 for pr in progress['pull_requests'] if pr['state'] == 'open'),
        'closed_prs': sum(1 for pr in progress['pull_requests'] if pr['state'] == 'closed'),
        'total_issues': len(progress['issues']),
        'open_issues': sum(1 for issue in progress['issues'] if issue['state'] == 'open'),
        'closed_issues': sum(1 for issue in progress['issues'] if issue['state'] == 'closed')
    }
    return summary

# Example usage:
# github_client = GitHubClient(os.getenv("GITHUB_TOKEN"))
# repo_name = "organization/student-assignment"
# progress, summary = track_student_progress(github_client, repo_name)
# print(summary)
# print(f"Recent commits: {progress['commits'][:5]}")  # Show 5 most recent commits
