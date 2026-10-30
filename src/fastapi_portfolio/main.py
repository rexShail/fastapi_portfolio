from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException
from pathlib import Path

app = FastAPI()

package_directory = Path(__file__).parent
app.mount(
    "/static",
    StaticFiles(directory=package_directory / "static"),
    name="static",
)

templates = Jinja2Templates(directory=package_directory / "templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Shail",
        "title": "Building APIs Quickly with FastAPI",
        "content": "FastAPI makes it simple to build fast, reliable APIs with automatic validation and clear documentation.",
        "date_posted": "October 28, 2026",
    },
    {
        "id": 2,
        "author": "Bandna Doe",
        "title": "Why Python Powers Modern Web Applications",
        "content": "Python combines readable syntax with a powerful ecosystem, making it a great choice for modern web development with FastAPI.",
        "date_posted": "October 29, 2026",
    },
    {
        "id": 3,
        "author": "Aarav Singh",
        "title": "Getting Started with REST API Design",
        "content": "Good API design starts with clear resources, predictable URLs, consistent responses, and meaningful HTTP status codes.",
        "date_posted": "October 30, 2026",
    },
    {
        "id": 4,
        "author": "Meera Patel",
        "title": "Testing FastAPI Applications",
        "content": "Automated tests help verify routes, validate response data, and catch regressions before changes reach production.",
        "date_posted": "November 2, 2026",
    },
    {
        "id": 5,
        "author": "Shail",
        "title": "Using Pydantic Models for Reliable Data",
        "content": "Pydantic models make incoming request data easier to validate and outgoing response data more consistent.",
        "date_posted": "November 5, 2026",
    },
    {
        "id": 6,
        "author": "Nisha Kapoor",
        "title": "Deploying a FastAPI Service",
        "content": "A successful deployment includes environment configuration, dependency management, health checks, and production logging.",
        "date_posted": "November 8, 2026",
    },
]


@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts": posts, "title": "Home"},
    )


@app.get("/posts/{post_id}", include_in_schema=False)
def post_page(request: Request, post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            title = post["title"][:50]
            return templates.TemplateResponse(
                request,
                "post.html",
                {"post": post, "title": title},
            )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


@app.get("/api/posts")
def get_posts():
    return posts


@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


@app.exception_handler(StarletteHTTPException)
def general_http_exception_handler(request: Request, exception: StarletteHTTPException):
    message = (
        exception.detail
        if exception.detail
        else "An error occurred. Please check your request and try again."
    )

    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=exception.status_code,
            content={"detail": message},
        )

    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": exception.status_code,
            "title": exception.status_code,
            "message": message,
        },
        status_code=exception.status_code,
    )


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={"detail": exception.errors()},
        )

    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "title": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "message": "Invalid request. Please check your input and try again.",
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
    )