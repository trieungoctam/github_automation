import os

def create_assignments(github_client, students, template_repo, organization):
    
    for student in students:
        repo_name = f"{organization}/{student}-assignment"
        github_client.create_repo(repo_name, organization)
        # Logic sao chép template_repo vào repo của sinh viên
