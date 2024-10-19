# API Documentation: GitHub Classroom Automation Tool
This API documentation describes the endpoints used to interact with the GitHub Classroom Automation Tool, which automates tasks such as creating repositories, tracking student progress, sending notifications, and grading assignments. The tool uses GitHub’s API to manage repositories, commits, and issues for student assignments.

## Base URL
- All API requests will interact with GitHub’s REST API.
- Base URL: https://api.github.com

## Authentication
- All API requests must include a valid GitHub Personal Access Token (PAT) in the request headers for authentication.
- Token scopes should include:
    - repo: Full control of private repositories.
    - user: Access user email for sending notifications.

## Endpoints
### 1. Create a New Repository for a Student
Creates a new private repository for a student under the specified GitHub organization.

- Endpoint: POST /orgs/{organization}/repos
- Request Method: POST
- Headers:
    - Authorization: token YOUR_GITHUB_TOKEN
    - Accept: application/vnd.github.v3+json
- Request Body:
```json
{
  "name": "student-assignment",
  "description": "Assignment repository for student",
  "private": true
}
```

- Response:
    - Success: Returns details of the newly created repository

```json
{
  "id": 123456789,
  "name": "student-assignment",
  "full_name": "organization/student-assignment",
  "private": true,
  "url": "https://api.github.com/repos/organization/student-assignment"
}
```

- Failure: Error message explaining why the repository was not created.

#### Example cURL Request:

```bash
curl -X POST \
  https://api.github.com/orgs/{organization}/repos \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -d '{"name":"student-assignment","description":"Assignment repository for student","private":true}'

```

### 2. List Commits for a Student’s Repository
Retrieves the list of commits from a specific student’s repository to track their progress.

- Endpoint: GET /repos/{owner}/{repo}/commits
- Request Method: GET
- Headers:
    - Authorization: token YOUR_GITHUB_TOKEN
    - Accept: application/vnd.github.v3+json
- Path Parameters:
    - {owner}: The GitHub organization or user who owns the repository.
    - {repo}: The name of the repository.
- Response:
    - Success: Returns an array of commits

```json
[
  {
    "sha": "abc123def456",
    "commit": {
      "message": "Initial commit",
      "author": {
        "name": "Student Name",
        "email": "student@example.com",
        "date": "2024-10-15T12:34:56Z"
      }
    },
    "html_url": "https://github.com/organization/student-assignment/commit/abc123def456"
  }
]

```
- Failure: Error message explaining why the commits could not be retrieved.

#### Example cURL Request:
```bash
curl -X GET \
  https://api.github.com/repos/{owner}/{repo}/commits \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json"
```

### 3. Create an Issue for a Student’s Repository
Creates a GitHub issue in the student’s repository to remind them to submit their work.

- Endpoint: POST /repos/{owner}/{repo}/issues
- Request Method: POST
- Headers:
    - Authorization: token YOUR_GITHUB_TOKEN
    - Accept: application/vnd.github.v3+json
- Request Body:
```json
{
  "title": "Reminder to submit your assignment",
  "body": "This is a friendly reminder to submit your assignment before the deadline."
}
```
- Response:
    - Success: Returns details of the newly created issue.
```json
    {
  "id": 987654321,
  "number": 1,
  "title": "Reminder to submit your assignment",
  "state": "open",
  "url": "https://api.github.com/repos/organization/student-assignment/issues/1"
}
```
    - Failure: Error message explaining why the issue could not be created.

#### Example cURL Request:
```bash
curl -X POST \
  https://api.github.com/repos/{owner}/{repo}/issues \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -d '{"title":"Reminder to submit your assignment","body":"This is a friendly reminder to submit your assignment before the deadline."}'
```

### 4. Trigger Auto-Grading Using GitHub Actions
This is a custom GitHub Actions workflow configured to run automated tests (syntax checks, unit tests) on the student’s repository.

- Trigger: The auto-grading is triggered when the student pushes their code to the repository.
- Configuration File: .github/workflows/main.yml in the student's repository.
- Response:
    - The results of the tests are posted as comments in the GitHub repository, either under issues or in the Pull Request, if applicable.

#### GitHub Actions Configuration Example:
```yaml
name: Auto Grading

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Check out repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        pip install -r requirements.txt

    - name: Run unit tests
      run: |
        pytest
```

## Rate Limits

- The GitHub API has rate limits depending on the type of token and the endpoints used.
- Authenticated requests: 5,000 requests per hour.
- Unauthenticated requests: 60 requests per hour.
- To check your rate limit:
    - Endpoint: GET /rate_limit
    - Response:
```json
{
  "rate": {
    "limit": 5000,
    "remaining": 4999,
    "reset": 1372700873
  }
}
```

## Error Handling
For all API requests, GitHub returns appropriate HTTP status codes:

- 200 OK: The request was successful.
- 201 Created: The repository or issue was successfully created.
- 400 Bad Request: There was an error in the request.
- 401 Unauthorized: Authentication failed (incorrect or missing token).
- 404 Not Found: The requested resource (e.g., repository) was not found.
- 500 Internal Server Error: A server error occurred.

Each response will contain a detailed error message when applicable. For example:
```json
{
  "message": "Validation Failed",
  "errors": [
    {
      "resource": "Issue",
      "field": "title",
      "code": "missing_field"
    }
  ]
}
```