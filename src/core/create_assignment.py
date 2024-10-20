import os
from src.utils.logger import github_classroom_logger
from typing import List, Dict

def create_assignments(github_client, students: List[str], template_repo: str, organization: str) -> List[Dict]:
    github_classroom_logger.info(f"Starting assignment creation for {len(students)} students")
    results = []
    
    for student in students:
        student_repo_name = f"{student}-assignment"
        full_repo_name = f"{organization}/{student_repo_name}"
        
        github_classroom_logger.info(f"Creating assignment for student: {student}")
        try:
            # Create the repository for the student
            github_classroom_logger.debug(f"Creating repository: {student_repo_name}")
            repo = github_client.create_repo(student_repo_name, organization)
            
            # Create student repo from template
            github_classroom_logger.debug(f"Creating student repo from template: {template_repo}")
            github_client.create_student_repo_from_template(
                template_owner=organization,
                template_repo=template_repo,
                student_repo_name=student_repo_name
            )
            
            # Set repository permissions for the student
            github_classroom_logger.debug(f"Setting repository permissions for: {student}")
            github_client.add_collaborator(full_repo_name, student, permission='push')
            
            # Create an initial issue for the student
            github_classroom_logger.debug(f"Creating welcome issue for: {student}")
            issue_title = "Welcome to your assignment!"
            issue_body = f"Hello {student},\n\nThis repository has been created for your assignment. Good luck!"
            github_client.create_issue(full_repo_name, issue_title, issue_body)
            
            github_classroom_logger.info(f"Assignment created successfully for: {student}")
            results.append({"student": student, "status": "success", "repo": full_repo_name})
        except Exception as e:
            github_classroom_logger.error(f"Error creating assignment for {student}: {str(e)}")
            results.append({"student": student, "status": "error", "message": str(e)})
    
    github_classroom_logger.info(f"Assignment creation completed. Successful: {sum(1 for r in results if r['status'] == 'success')}, Failed: {sum(1 for r in results if r['status'] == 'error')}")
    return results

# Example usage:
# from src.client.github_client import GitHubClient
# from src.utils.config import settings
# 
# github_client = GitHubClient(settings.GITHUB_TOKEN)
# students = ["student1", "student2", "student3"]
# template_repo = "assignment-template"
# organization = "your-org-name"
# results = create_assignments(github_client, students, template_repo, organization)
