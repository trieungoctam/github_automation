# Architecture Document: GitHub Classroom Automation Tool

## 1. Overview
This document outlines the system architecture of the GitHub Classroom Automation Tool, designed to automate several manual tasks such as creating repositories for students, tracking their progress, sending notifications, and grading assignments using GitHub Actions.

The architecture follows a modular approach to provide flexibility, scalability, and maintainability. The tool interacts with GitHub’s API for automating tasks and integrates external services like email for notifications. It is primarily built in Python and supports CI/CD pipelines via GitHub Actions for auto-grading student submissions.

## 2. Key Components
The architecture of the tool consists of the following major components:

1. GitHub API Client (GitHubClient):
- Handles all interactions with the GitHub API.
- Responsible for creating repositories, managing issues, and retrieving repository data.
2. Assignment Management:
- Automates the creation of assignments by cloning templates into new repositories for students.
3. Progress Tracker:
- Tracks the number of commits and progress of students for each assignment.
- Retrieves data from the GitHub API to monitor the activity of each student.
4. Notification System:
- Sends automated reminders via GitHub Issues or email if students are behind schedule.
5. Auto-Grading System:
- Uses GitHub Actions to run automated tests (syntax checks, unit tests) when students push code to their repositories.

## 3. System Architecture Diagram

```
+-------------------------+    +-------------------------------------+
|   Student’s GitHub Repo  |<---|  Assignment Template Repository     |
+-------------------------+    +-------------------------------------+
           |                                   ^
           v                                   |
+----------------------------+     +--------------------------+
|    GitHub API Client        |---->| GitHub API               |
+----------------------------+     +--------------------------+
           |                                   
           v                                       
+--------------------------------+                           
|       Progress Tracker         |                           
+--------------------------------+                           
           |                                   
           v                                   
+--------------------------------+                           
|    Notification System         |                           
+--------------------------------+                           
           |                                   
           v                                   
+--------------------------------+                           
|        Auto-Grading System     |                           
|      (via GitHub Actions)      |                           
+--------------------------------+                           
```

## 4. Design Decisions
4.1. GitHub API Client
- Purpose: To simplify all interactions with GitHub’s API, including creating repositories, fetching commit data, and managing issues.
- Why: GitHub provides a REST API that allows interaction with repositories, commits, and issues. Centralizing these operations in a client class improves modularity and reusability.
- Example Operations:
    - Creating a new repository for each student.
    - Fetching the number of commits from a student's repository.
    - Posting issues for automatic notifications.

4.2. Assignment Management
- Purpose: Automatically create and distribute coding assignments.
- Why: Manually creating repositories for each student is time-consuming. By automating this process, each student can receive their assignment without teacher intervention.
- Operation:
    - Cloning the assignment template from a base repository.
    - Creating new repositories for students based on their GitHub usernames.

4.3. Progress Tracking
- Purpose: Monitor student activity by tracking the number of commits they make to their repositories.
- Why: Teachers need a way to monitor whether students are progressing with their work.
- Operation:
    - Polling each student’s repository to count the number of commits.
    - Providing an overview of student activity for teacher review.

4.4. Notification System
- Purpose: Send automatic reminders if a student is behind schedule.
- Why: Teachers should not have to manually remind students to submit assignments. Automated reminders help keep students on track.
- Notifications:
    - Email: Sent via an SMTP server integrated into the system.
    - GitHub Issues: Automatically created in the student's repository if they are late.

4.5. Auto-Grading System
- Purpose: Automatically check students’ code submissions by running syntax checks and unit tests when they push changes to GitHub.
- Why: Automated testing ensures that basic code quality and functionality are met without manual review for every submission.
- Implementation:
    - GitHub Actions triggers on every push to a student’s repository.
    - Configured to run unit tests, check coding standards, and report results to both the student and teacher.

## 5. Workflow
1. Assignment Creation:
- The system automatically creates individual repositories for each student and clones an assignment template into their repository.
2. Student Submission:
- Students work on their assignments and push their code to GitHub.
3. Tracking Progress:
- The system periodically checks the number of commits and provides updates to the teacher.
4. Notification System:
- If a student has not submitted their work by a certain deadline, the system sends a reminder via GitHub Issues or email.
5. Auto-Grading:
- When a student pushes code, GitHub Actions automatically runs tests on their submission and provides feedback via issues or email.


## 6. Technologies Used
- Backend:

    - Python: Primary language for API interactions, progress tracking, and notifications.
    - GitHub API: Used to manage repositories, issues, and commits.
- Notification System:

    - SMTP (Email): For sending email reminders to students.
    - GitHub Issues: For creating issues in student repositories as reminders.
- Continuous Integration:

    - GitHub Actions: For running automated tests and providing immediate feedback to students.

## 7. Scalability Considerations
- Multi-class Support: The system can be extended to support multiple classes by adding a layer of abstraction for handling multiple repositories and classrooms.

- Repository Limits: GitHub has rate limits on API requests. Caching and batching requests are considered to ensure the system can scale across many students and repositories without hitting API limits.

- Parallel Processing: For large classrooms, progress tracking, and grading tasks can be parallelized to improve efficiency.

## 8. Deployment
The tool can be deployed on any server that supports Python and has access to the GitHub API. Below are the suggested deployment strategies:

1. Local Deployment:

    - Suitable for development and small-scale testing.
    - Use a local machine to run the tool.
2. Cloud Deployment:

    - Suitable for larger classrooms and environments where continuous operation is required.
Recommended platforms: AWS, Google Cloud, Heroku.
3. Dockerized Deployment:

    - A Docker image can be built for easier deployment across multiple environments.
    - Ideal for Kubernetes or containerized environments.

## 9. Security Considerations
- GitHub Personal Access Token (PAT):

    - The token should be stored securely using environment variables.
    - Use minimal scopes required for the project (repository access, issue management).
- Email Server Credentials:

    - Store email server credentials securely and use encrypted communication (TLS/SSL) when sending notifications.
- Student Data:

    - Ensure that sensitive information such as email addresses is not exposed in public repositories.

## 10. Conclusion
This architecture allows the GitHub Classroom Automation Tool to function efficiently and flexibly across various classroom settings. It reduces manual effort for teachers, improves the student experience through real-time feedback, and is easily extensible to support additional features or classrooms. By leveraging GitHub’s API, automated grading, and notification systems, this tool provides a scalable solution for managing programming assignments.