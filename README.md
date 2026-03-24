# Dog Vaccine Tracker

A full-stack web application to track dog vaccinations, manage multiple dogs, and calculate upcoming vaccine schedules.

## Overview

Dog Vaccine Tracker lets you keep a complete vaccination history for one or more dogs and automatically calculates which vaccines are current, upcoming (within 30 days), or overdue — based on each vaccine's recurrence interval.

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Angular 17+, TypeScript, Angular Material |
| Backend | Python 3.12, FastAPI |
| Database | PostgreSQL (production), SQLite (dev) |
| ORM | SQLAlchemy + Alembic |
| Containerization | Docker, Docker Compose |
| Orchestration | Kubernetes (Minikube for local) |
| CI/CD | GitHub Actions |
| Testing | Pytest (backend), Jasmine/Karma (frontend) |

## Architecture

Three-tier application:

- **Frontend (Angular)** — served via Nginx, communicates with the backend over REST.
- **Backend (FastAPI)** — handles business logic, CRUD operations, and vaccine schedule calculations.
- **Database (PostgreSQL)** — persistent storage managed via SQLAlchemy and Alembic migrations.

Dev environment runs via Docker Compose; production targets Kubernetes.
