# Troubleshooting Documentation: GitHub Classroom Automation Tool
This troubleshooting guide is designed to help resolve common issues that may arise during the deployment or operation of the GitHub Classroom Automation Tool. It addresses problems related to API requests, notifications, GitHub Actions, and deployment issues on various platforms.

## 1. GitHub API Issues
### 1.1. API Rate Limiting
Problem: You encounter a 403 Forbidden error with a message indicating rate limiting by the GitHub API.

Cause: GitHub limits the number of API requests based on authentication type. If you exceed the limit (5,000 requests per hour for authenticated users), the API will deny further requests.

Solution:

- Check the current rate limit by sending a request to https://api.github.com/rate_limit.
- Optimize your code to reduce the number of API requests, such as caching results or batching API calls.
- Use a GitHub Personal Access Token (PAT) with proper scopes for authentication, as it increases the rate limit compared to unauthenticated requests.
- Consider using multiple tokens for large classrooms or periods of high API activity.
#### Example API Rate Limit Check:

```bash
curl -H "Authorization: token YOUR_GITHUB_TOKEN" https://api.github.com/rate_limit
```
### 1.2. GitHub API Authentication Failure
Problem: API requests return a 401 Unauthorized error.

Cause: Invalid or missing GitHub Personal Access Token (PAT).

Solution:

- Ensure that the token is included in the request headers as follows:

```bash
Authorization: token YOUR_GITHUB_TOKEN
```
- Verify that the token has the necessary permissions (repo access and user access).

- Ensure the token is not expired and has been correctly stored in the .env file or your environment variables.

- Double-check your .env file format to make sure there are no spaces around the equal sign or newlines between the variables.

### 1.3. Repository Not Created
Problem: Repository creation fails with a 400 Bad Request error or does not appear in the organization.

Cause: Incorrect request body, invalid organization name, or insufficient permissions.

Solution:

- Check that the organization name is correct and that you have permission to create repositories within that organization.
- Verify that the request body includes the required fields, such as name and private status.
- Ensure that the token has repo scope to allow repository creation in the organization.
#### Example cURL Command for Creating a Repository:

```bash
curl -X POST \
  https://api.github.com/orgs/{organization}/repos \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -d '{"name":"student-assignment","private":true}'
```

## 2. Notification Issues

### 2.1. Email Notifications Not Sending
Problem: Emails are not being sent, or you encounter an SMTP connection error.

Cause: Misconfigured SMTP server settings or incorrect email credentials.

Solution:

- Ensure that the SMTP server address, port, email, and password are correctly configured in the .env file.
- Verify that the SMTP port is correct (usually 465 for SSL or 587 for TLS).
- Ensure that you have enabled "Less secure apps" for your Gmail account if you're using Gmail as the email server. Alternatively, use an App password if two-factor authentication (2FA) is enabled on your account.
- Make sure your email server allows external connections and that no firewalls or security settings are blocking outbound emails.
#### Example Email Configuration in .env:

```bash
EMAIL_SERVER=smtp.gmail.com
EMAIL_PORT=465
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_password
```
### 2.2. GitHub Issues Not Created for Notifications
Problem: GitHub issues are not created as expected for student reminders.

Cause: Incorrect repository name or insufficient permissions.

Solution:

- Ensure the repository name is correct and accessible by the GitHub API client.
- Make sure that the GitHub token has repo and issues scopes to allow issue creation.
- Double-check the API request body for creating an issue, ensuring it contains the required title and body fields.
#### Example cURL Command for Creating an Issue:

```bash
curl -X POST \
  https://api.github.com/repos/{owner}/{repo}/issues \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -d '{"title":"Reminder to submit your assignment","body":"Please submit your assignment before the deadline."}'
```

## 3. GitHub Actions Failing
### 3.1. GitHub Actions Not Triggering
Problem: GitHub Actions are not triggered when students push their code to the repository.

Cause: Incorrect workflow configuration or missing .github/workflows/main.yml file.

Solution:

- Ensure that the .github/workflows/main.yml file is present in the student’s repository and properly configured to trigger on push events.
- Check that the correct branch (e.g., main or master) is specified in the workflow file.
- Validate the YAML syntax in the GitHub Actions configuration file.
#### Example Workflow Trigger:

```yaml
name: Auto Grading

on:
  push:
    branches:
      - main
```
### 3.2. GitHub Actions Failing to Run Tests
Problem: GitHub Actions trigger but fail to execute the test suite or build.

Cause: Missing dependencies or incorrect Python version.

Solution:

- Verify that all dependencies are correctly listed in the requirements.txt file and are installed in the workflow.
- Check that the correct Python version is set in the GitHub Actions workflow file.
- Use GitHub Actions logs to identify specific errors during the execution of the workflow.
#### Example Step to Install Dependencies in GitHub Actions:

```yaml
steps:
  - name: Install dependencies
    run: pip install -r requirements.txt
```
## 3.3. GitHub Actions Rate Limit Exceeded
Problem: GitHub Actions fail due to API rate limits, especially in large classrooms.

Cause: Too many API requests within a short time frame.

Solution:

- Spread out push events by asking students to submit their assignments in batches.
- Optimize the number of API calls made by the workflow.
- Consider using multiple GitHub tokens with different rate limits for larger classrooms.