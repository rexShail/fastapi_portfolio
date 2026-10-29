# FastAPI Portfolio

A portfolio-style blog homepage and JSON API built with FastAPI and Jinja templates. It demonstrates a package-based FastAPI application, server-rendered HTML, static assets, and interactive API documentation.

## Features

- Server-rendered homepage with a responsive Bootstrap layout
- Blog posts served from the application
- JSON posts endpoint
- Local SVG profile pictures and site icons
- Automatic Swagger UI and ReDoc documentation
- Development auto-reload with FastAPI's CLI

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/) for dependency and environment management

## Installation

Clone the repository and install the project dependencies:

```bash
git clone https://github.com/rexShail/fastapi_portfolio.git
cd fastapi_portfolio
uv sync
```

## Run the application

Start the development server from the project directory:

```bash
uv run fastapi dev main.py
```

Open:

- Homepage: http://127.0.0.1:8000/
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Posts API: http://127.0.0.1:8000/api/posts

## API endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Portfolio and blog homepage |
| `GET` | `/api/posts` | Return the list of blog posts as JSON |
| `GET` | `/docs` | Interactive Swagger UI |
| `GET` | `/redoc` | ReDoc API documentation |

## Project structure

```text
fastapi_portfolio/
├── main.py                         # FastAPI entry point
├── pyproject.toml                  # Project metadata and dependencies
├── src/
│   └── fastapi_portfolio/
│       ├── main.py                 # Application routes and sample data
│       ├── templates/
│       │   ├── layout.html         # Shared page layout
│       │   └── home.html           # Homepage template
│       └── static/
│           ├── css/main.css        # Custom styles
│           ├── icons/              # Favicon and app icons
│           └── profile_pics/       # Author profile illustrations
└── README.md
```

## Development

FastAPI watches the project and reloads when source or template files change. Stop the server with `Ctrl+C`.

If port `8000` is already occupied, start the server on another port:

```bash
uv run fastapi dev main.py --port 8001
```

## License

This project does not yet include a license. Add one if you plan to publish or distribute the project.