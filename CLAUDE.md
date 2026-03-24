# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A full-stack web application to track dog vaccinations, manage multiple dogs, and calculate upcoming vaccine schedules.

- **Frontend**: Angular 17+, TypeScript, Angular Material (served via Nginx)
- **Backend**: Python 3.12, FastAPI
- **Database**: PostgreSQL (prod) / SQLite (dev), managed via SQLAlchemy + Alembic
- **Dev**: Docker Compose; **Prod**: Kubernetes

## Repository Structure

```
backend/    # Python/FastAPI service
frontend/   # Angular application
docs/       # Documentation
k8s/        # Kubernetes manifests
```

## Setup

This project has not been initialized yet. Once dependencies are set up, update this file with:
- How to install dependencies and run dev servers
- How to run tests (`pytest` for backend, `ng test` for frontend)
- Required environment variables
