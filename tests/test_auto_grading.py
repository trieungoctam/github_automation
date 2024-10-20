import pytest
from unittest.mock import Mock, patch
from src.core.auto_grading import auto_grade
from src.client.github_client import GitHubClient

@pytest.fixture
def mock_github_client():
    return Mock(spec=GitHubClient)

@pytest.fixture
def sample_repo_content():
    return {
        "path": "test_file.py",
        "content": "ZGVmIGFkZChhLCBiKToKICAgIHJldHVybiBhICsgYg=="  # Base64 encoded: def add(a, b):\n    return a + b
    }

@patch('src.core.auto_grading.base64.b64decode')
def test_auto_grade_correct_implementation(mock_b64decode, mock_github_client, sample_repo_content):
    mock_github_client.get_file_content.return_value = sample_repo_content
    mock_b64decode.return_value = b"def add(a, b):\n    return a + b"

    result = auto_grade(mock_github_client, "test_repo", "test_file.py", "add")

    assert result["passed"] == True
    assert result["feedback"] == "Great job! Your implementation is correct."

@patch('src.core.auto_grading.base64.b64decode')
def test_auto_grade_incorrect_implementation(mock_b64decode, mock_github_client, sample_repo_content):
    mock_github_client.get_file_content.return_value = sample_repo_content
    mock_b64decode.return_value = b"def add(a, b):\n    return a - b"  # Incorrect implementation

    result = auto_grade(mock_github_client, "test_repo", "test_file.py", "add")

    assert result["passed"] == False
    assert "Your implementation is incorrect" in result["feedback"]

@patch('src.core.auto_grading.base64.b64decode')
def test_auto_grade_syntax_error(mock_b64decode, mock_github_client, sample_repo_content):
    mock_github_client.get_file_content.return_value = sample_repo_content
    mock_b64decode.return_value = b"def add(a, b):\n    return a + b:"  # Syntax error

    result = auto_grade(mock_github_client, "test_repo", "test_file.py", "add")

    assert result["passed"] == False
    assert "Syntax error in your code" in result["feedback"]

def test_auto_grade_file_not_found(mock_github_client):
    mock_github_client.get_file_content.side_effect = Exception("File not found")

    result = auto_grade(mock_github_client, "test_repo", "non_existent_file.py", "add")

    assert result["passed"] == False
    assert "Error: Unable to retrieve the file content" in result["feedback"]

