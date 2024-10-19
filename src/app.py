from src.core.create_assignment import create_assignments
from src.core.track_progress import track_student_progress
from src.core.auto_grading import auto_grade
from client.github_client import GitHubClient

if __name__ == "__main__":
    students = ["student1", "student2", "student3"]
    template_repo = "organization/template-repo"
    organization = "LTM-PTIT"

    github_client = github_client = GitHubClient(token=os.getenv("GITHUB_TOKEN"))

    # Tạo bài tập
    create_assignments(github_client, students, template_repo, organization)

    # Theo dõi tiến độ
    for student in students:
        progress = track_student_progress(github_client, f"{organization}/{student}-assignment")
        print(f"Progress for {student}: {progress} commits")

    # Tự động chấm bài
    for student in students:
        auto_grade(f"{organization}/{student}-assignment")
