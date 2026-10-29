from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(title="FastAPI Portfolio", version="1.0.0")
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
]

@app.get("/", response_class=HTMLResponse       )
def read_root():
    return """
    <h1>Welcome to the FastAPI Portfolio!</h1>
    """

@app.get("/api/posts", response_class=JSONResponse)
def get_posts():
    return posts