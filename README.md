# Python HTTP Server

A simple HTTP server built from scratch using Python's `socket` library, no frameworks, no dependencies.

Built to understand how HTTP works at a low level.

## Features

- Handles GET requests
- Serves HTML pages
- Returns a custom 404 page for unknown routes

## How to Run

```bash
python myserver.py
```

Then open your browser and go to: `http://127.0.0.1:8080`

## Project Structure
```
python-http-server/
├── server.py       # Core server logic
├── index.html      # Home page
├── 404.html        # Not found page
└── README.md
```
## Planned Improvements

- [ ] Multithreading to handle multiple clients
- [ ] Support for POST, PUT, DELETE methods
- [ ] Dynamic static file serving

## Tech

- Python 3
- `socket` standard library only
