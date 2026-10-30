# FastAPI Portfolio

A server-rendered portfolio blog built with FastAPI, Jinja templates, and Bootstrap. The project also exposes a small JSON API and custom HTML and JSON error responses.

## Features

- Responsive Bootstrap blog layout
- Home and `/posts` listing pages
- Individual post pages at `/posts/{post_id}`
- JSON endpoints for all posts and individual posts
- Custom HTML pages for HTTP and validation errors
- Package-relative templates and static assets
- Local SVG profile pictures and icons
- Interactive Swagger UI and ReDoc documentation

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/) for dependency and virtual environment management

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/rexShail/fastapi_portfolio.git
cd fastapi_portfolio
uv sync
```

## Run locally

Start the development server:

```bash
uv run fastapi dev main.py
```

Then open:

- Home page: http://127.0.0.1:8000/
- Posts page: http://127.0.0.1:8000/posts
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Posts API: http://127.0.0.1:8000/api/posts

Stop the server with `Ctrl+C`.

## Routes

### HTML routes

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Blog home page |
| `GET` | `/posts` | Blog post listing |
| `GET` | `/posts/{post_id}` | Individual post page |

### JSON API routes

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/api/posts` | Return all posts |
| `GET` | `/api/posts/{post_id}` | Return one post |

API documentation is available at `/docs`, and an alternative ReDoc view is available at `/redoc`.

## Example API request

```bash
curl http://127.0.0.1:8000/api/posts/1
```

Example response:

```json
{
  "id": 1,
  "author": "Shail",
  "title": "Building APIs Quickly with FastAPI",
  "content": "FastAPI makes it simple to build fast, reliable APIs with automatic validation and clear documentation.",
  "date_posted": "October 28, 2026"
}
```

## Project structure

```text
fastapi_portfolio/
├── main.py
├── pyproject.toml
├── src/fastapi_portfolio/
│   ├── __init__.py
│   ├── main.py
│   ├── static/
│   │   ├── css/
│   │   ├── icons/
│   │   └── profile_pics/
│   └── templates/
│       ├── layout.html
│       ├── home.html
│       ├── post.html
│       └── error.html
└── README.md
```

## Development

The development server watches the project and reloads changed Python and template files automatically.

If port `8000` is already in use, select another port:

```bash
uv run fastapi dev main.py --port 8001
```

## License

No license has been added yet.