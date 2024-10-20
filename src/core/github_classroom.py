from github import Github
from typing import List
from datetime import datetime, timedelta
from src.utils.logger import github_classroom_logger

class GitHubClassroom:
    def __init__(self, token: str):
        self.github = Github(token)
        github_classroom_logger.info("GitHubClassroom instance created")

    def create_assignment(self, classroom_id: str, assignment_name: str, repo_template: str):
        github_classroom_logger.info(f"Creating assignment: {assignment_name} for classroom: {classroom_id}")
        try:
            org = self.github.get_organization(classroom_id)
            template_repo = self.github.get_repo(repo_template)
            new_repo = org.create_repo(
                name=assignment_name,
                description=f"Assignment: {assignment_name}",
                private=True,
                template=True
            )
            new_repo.create_from_template(template_repo)
            github_classroom_logger.info(f"Assignment created successfully: {new_repo.html_url}")
            return new_repo
        except Exception as e:
            github_classroom_logger.error(f"Error creating assignment: {str(e)}")
            raise

    def create_student_repo(self, classroom_id: str, assignment_name: str, student_github_username: str):
        github_classroom_logger.info(f"Creating student repo for {student_github_username}, assignment: {assignment_name}")
        try:
            org = self.github.get_organization(classroom_id)
            template_repo = org.get_repo(assignment_name)
            student_repo = org.create_repo(
                name=f"{assignment_name}-{student_github_username}",
                description=f"Assignment for {student_github_username}",
                private=True
            )
            student_repo.create_from_template(template_repo)
            student_repo.add_to_collaborators(student_github_username, permission="push")
            github_classroom_logger.info(f"Student repo created successfully: {student_repo.html_url}")
            return student_repo
        except Exception as e:
            github_classroom_logger.error(f"Error creating student repo: {str(e)}")
            raise

    def check_student_progress(self, repo_name: str, days: int = 30):
        github_classroom_logger.info(f"Checking student progress for repo: {repo_name}, last {days} days")
        try:
            repo = self.github.get_repo(repo_name)
            since_date = datetime.now() - timedelta(days=days)
            commits = repo.get_commits(since=since_date)
            issues = repo.get_issues(state='all', since=since_date)
            pull_requests = repo.get_pulls(state='all')
            
            progress = {
                'commits': [{'sha': c.sha, 'message': c.commit.message} for c in commits],
                'issues': [{'number': i.number, 'title': i.title, 'state': i.state} for i in issues],
                'pull_requests': [{'number': pr.number, 'title': pr.title, 'state': pr.state} for pr in pull_requests]
            }
            github_classroom_logger.info(f"Progress check completed for {repo_name}")
            return progress
        except Exception as e:
            github_classroom_logger.error(f"Error checking student progress: {str(e)}")
            raise

    def auto_grade(self, repo_name: str):
        github_classroom_logger.info(f"Starting auto-grading for repo: {repo_name}")
        try:
            repo = self.github.get_repo(repo_name)
            # This is a placeholder. Real auto-grading would involve running tests, etc.
            latest_commit = repo.get_commits()[0]
            grade = 100  # placeholder grade
            repo.create_issue(
                title="Auto-grading results",
                body=f"Grade for commit {latest_commit.sha}: {grade}/100"
            )
            github_classroom_logger.info(f"Auto-grading completed for {repo_name}. Grade: {grade}")
            return grade
        except Exception as e:
            github_classroom_logger.error(f"Error during auto-grading: {str(e)}")
            raise
