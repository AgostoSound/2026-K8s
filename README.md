# 2026-K8s — Django API with PostgreSQL (Local → Docker → Kubernetes)

Backend API built with **Django + Django REST Framework** using **PostgreSQL** as database, designed to run **100% locally with Docker** and later be deployed to **Kubernetes**.

This project focuses on **end-to-end backend fundamentals**: API design, database persistence, Dockerized services, and reproducible local environments.

---

## 🚀 Tech Stack

- **Python 3.11**
- **Django 5**
- **Django REST Framework**
- **PostgreSQL 16**
- **Docker & Docker Compose**
- **DBeaver** (DB inspection)
- **Git / GitHub**

---

## 📂 Project Structure

```text
2026-K8s/
├── api/                    # Main Django app
│   ├── models/             # Domain models
│   ├── serializers/        # DRF serializers
│   ├── views/              # API viewsets
│   ├── migrations/
│   └── admin/
├── config/                 # Django project settings
├── docker-compose.yml      # PostgreSQL service
├── requirements.txt
├── manage.py
├── .env.example            # Environment variables template
└── README.md
