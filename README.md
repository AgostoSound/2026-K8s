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
```

---

## 🧠 Domain Models

- **User** (Django built-in)
- **Product**
- **Reservation**
- **Rate**

Relations are handled via Django ORM and managed through migrations.

---

## 🐘 PostgreSQL (Dockerized)

PostgreSQL runs inside a Docker container with a **persistent volume**, meaning data survives restarts.

```yaml
services:
  postgres:
    image: postgres:16
    volumes:
      - pgdata:/var/lib/postgresql/data
```

⚠️ Data is only lost if the volume is explicitly removed.

---

## ⚙️ Environment Variables

The project uses a local `.env` file (not tracked by Git).

Example:

```env
DEBUG=1
DJANGO_SECRET_KEY=change-me

DB_NAME=api-k8s
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

Docker Compose automatically loads this file.

---

## ▶️ Local Setup

### 1. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start PostgreSQL
```bash
docker compose up -d
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create superuser
```bash
python manage.py createsuperuser
```

### 6. Start the server
```bash
python manage.py runserver
```

---

## 🔐 Django Admin

Access admin panel at:

```
http://127.0.0.1:8000/admin/
```

Use the superuser credentials created earlier.

---

## 🔌 API Endpoints

Base URL:
```
/api/
```

Available endpoints:
- `GET /api/products/`
- `GET /api/reservations/`
- `GET /api/rates/`

All endpoints are implemented using **DRF ViewSets**.

---

## 🧪 Database Inspection

You can connect to PostgreSQL using **DBeaver**:

- Host: `localhost`
- Port: `5432`
- Database: `api-k8s`
- User / Password: from `.env`

Useful for inspecting tables and validating migrations.

---

## 🧱 Persistence Model

- Docker **containers** can be stopped/restarted safely
- Docker **volumes** persist all database data
- Admin users and records survive restarts

```bash
docker compose stop   # safe
docker compose start  # safe
```

⚠️ This will delete data:
```bash
docker compose down -v
```

---

## 📦 Current Status

- ✅ Django API running locally
- ✅ PostgreSQL running in Docker
- ✅ Persistent database volume
- ✅ Admin interface enabled
- ✅ CRUD endpoints implemented
- ⏳ Dockerized API (next)
- ⏳ Kubernetes deployment (next)

---

## 🎯 Roadmap

- Dockerize Django API
- Add authentication & permissions
- Kubernetes manifests (Deployment, Service, PVC)
- Local cluster with `kind`
- Production-like environment simulation

---

## 👤 Author

**Augusto**  
Software Developer  
Amsterdam / NL

---

## 📄 License

MIT
