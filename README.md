# Welcome to my FastAPI Web Server Example
This repository's main purpose is to provide an educational resource that showcases how to use FastAPI in conjunction with SQLAlchemy/PostgreSQL to develop REST API endpoints for web applications with persistence.

> 📝 **Disclaimer**: still need for improvements and more in-depth documentation ✍️

## Quick Showcase
start with `docker compose up`
then navigate to [server's endpoint documentation](http://127.0.0.1:8080/docs)

## Rough Project Structure
- [.env](.env): global dotenv-file for configruation
- [compose.yml](compose.yml): docker compose file
- [README.md](README.md): this readme
- [.gitignore](.gitignore)
- [app/](app/): fastapi server application directory
    - [Dockerfile](app/Dockerfile)
    - [requirements.txt](app/requirements.txt)
    - [src/](app/src/)
        - [model/](app/src/model): the database's tables, CRUD operations, a DB-Manager for postgres connection and pydantic schemes are defined here
        - [view/](app/src/view): contains static servable files and dynamic Jinja templates to be rendered
        - [controller/](app/src/controller): contains the main.py for fastapi server app and the routing logic of requests to the endpoints



