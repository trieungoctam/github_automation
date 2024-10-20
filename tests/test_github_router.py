from fastapi.testclient import TestClient
from src.main import app
from unittest.mock import patch, MagicMock

client = TestClient(app)

@patch('src.client.github_client.GitHubClient')
def test_create_assignment_for_students(mock_github_client):
    mock_instance = MagicMock()
    mock_github_client.return_value = mock_instance

    mock_instance.create_repo_from_template.return_value = {"html_url": "https://github.com/org/repo"}
    mock_instance.add_collaborator.return_value = {}

    response = client.post(
        "/github/assignments/create",
        json={
            "assignment": {
                "name": "Assignment1",
                "description": "First assignment",
                "template_repo": "org/template-repo"
            },
            "students": [
                {"github_username": "student1"},
                {"github_username": "student2"}
            ]
        }
    )

    assert response.status_code == 200
    assert len(response.json()["results"]) == 2
    assert response.json()["results"][0]["student"] == "student1"
    assert response.json()["results"][1]["student"] == "student2"

    mock_instance.create_repo_from_template.assert_called()
    mock_instance.add_collaborator.assert_called()
