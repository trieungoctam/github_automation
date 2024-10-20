from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from src.utils.config import settings
from src.core.github_classroom import GitHubClassroom
from src.utils.logger import github_classroom_logger
from src.routers import github_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    docs_url=settings.DOCS_URL,
    openapi_url=settings.OPENAPI_URL,
)

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

def get_github_classroom():
    return GitHubClassroom(settings.GITHUB_TOKEN)

class AssignmentCreate(BaseModel):
    classroom_id: str
    assignment_name: str
    repo_template: str

class StudentRepoCreate(BaseModel):
    classroom_id: str
    assignment_name: str
    student_github_username: str

# app.include_router(github_router.router, prefix="/github", tags=["github"])

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}"}

# @app.post("/github/create-assignment")
# async def create_assignment(data: AssignmentCreate, github: GitHubClassroom = Depends(get_github_classroom)):
#     try:
#         github_classroom_logger.info(f"API request: Create assignment {data.assignment_name}")
#         repo = github.create_assignment(data.classroom_id, data.assignment_name, data.repo_template)
#         return {"message": "Assignment created", "repo_url": repo.html_url}
#     except Exception as e:
#         github_classroom_logger.error(f"API error: Create assignment failed - {str(e)}")
#         raise HTTPException(status_code=400, detail=str(e))

# @app.post("/github/create-student-repo")
# async def create_student_repo(data: StudentRepoCreate, github: GitHubClassroom = Depends(get_github_classroom)):
#     try:
#         github_classroom_logger.info(f"API request: Create student repo for {data.student_github_username}")
#         repo = github.create_student_repo(data.classroom_id, data.assignment_name, data.student_github_username)
#         return {"message": "Student repo created", "repo_url": repo.html_url}
#     except Exception as e:
#         github_classroom_logger.error(f"API error: Create student repo failed - {str(e)}")
#         raise HTTPException(status_code=400, detail=str(e))

# @app.get("/github/student-progress/{repo_name}")
# async def get_student_progress(repo_name: str, github: GitHubClassroom = Depends(get_github_classroom)):
#     try:
#         github_classroom_logger.info(f"API request: Get student progress for {repo_name}")
#         progress = github.check_student_progress(repo_name)
#         return {"message": "Student progress retrieved", "progress": progress}
#     except Exception as e:
#         github_classroom_logger.error(f"API error: Get student progress failed - {str(e)}")
#         raise HTTPException(status_code=400, detail=str(e))

# @app.post("/github/auto-grade/{repo_name}")
# async def auto_grade(repo_name: str, github: GitHubClassroom = Depends(get_github_classroom)):
#     try:
#         github_classroom_logger.info(f"API request: Auto-grade repo {repo_name}")
#         grade = github.auto_grade(repo_name)
#         return {"message": "Auto-grading completed", "grade": grade}
#     except Exception as e:
#         github_classroom_logger.error(f"API error: Auto-grading failed - {str(e)}")
#         raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    github_classroom_logger.info("Starting the GitHub Classroom Assistant application")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
