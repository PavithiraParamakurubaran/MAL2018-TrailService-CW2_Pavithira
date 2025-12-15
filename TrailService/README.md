# 🌄 TrailService Microservice

---

## Overview

**TrailService** is a Python-based microservice developed for the **MAL2018 Information Management & Retrieval** module. It provides CRUD operations for trail data, including:

* Trail names & descriptions
* Difficulty levels
* GPS points
* Trail features
* Trail photos

The microservice interacts with an external **Authenticator API** to validate users and ensures secure, structured data management.

---

## Tech Stack

* **Python 3.12** with FastAPI
* **Microsoft SQL Server** for persistent storage
* **Docker Desktop** for containerized database
* **Azure Data Studio** for database management (optional)
* **Swagger / OpenAPI** for interactive API documentation

---

## Repository Structure

```
TrailService/
│
├── app/                    # Python application code
│   ├── main.py             # FastAPI entry point
│   ├── database.py         # Database connection logic
│   ├── models.py           # Pydantic schemas
│   ├── crud.py             # CRUD operations
│   ├── routers.py          # API endpoints
│   └── utils.py            # Helper functions
│
├── sql/                    # Database scripts
│   ├── cw2_schema.sql      # Table creation
│   ├── procedures.sql      # Stored procedures
│   ├── trigger.sql         # Trigger for TrailLog
│   ├── views.sql           # Views for aggregated trail info
│   └── sample_data.sql     # Sample data for testing
│
├── requirements.txt        # Python dependencies
└── README.md               # Documentation (this file)
```

---

## Prerequisites

* Python 3.12+
* Docker Desktop (for SQL Server container)
* Microsoft SQL Server 2022 Docker image
* Azure Data Studio (optional, for managing DB)

---

## Setup & Running

### 1️⃣ Start SQL Server

```bash
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=C0mp2001!" \
-p 1433:1433 -d mcr.microsoft.com/mssql/server:2022-latest
```

### 2️⃣ Apply SQL Scripts

Run in Azure Data Studio or any SQL client, in the following order:

1. `cw2_schema.sql`
2. `procedures.sql`
3. `trigger.sql`
4. `views.sql`
5. `sample_data.sql` *(optional)*

### 3️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run FastAPI Service

```bash
uvicorn app.main:app --reload
```

**Access the service at:**

* Base URL: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Testing the API

Use **Swagger UI**, Postman, or any HTTP client.

### Endpoints

| Method | Endpoint       | Description               |
| ------ | -------------- | ------------------------- |
| POST   | `/trails`      | Create a new trail        |
| GET    | `/trails`      | Retrieve all trails       |
| GET    | `/trails/{id}` | Retrieve a specific trail |
| PUT    | `/trails/{id}` | Update trail details      |
| DELETE | `/trails/{id}` | Delete a trail            |

All endpoints return **JSON responses** and enforce data integrity using **Pydantic validation**.

---

## Security & Data Integrity

* Authentication via **external Authenticator API**
* No sensitive data stored locally
* Parameterized queries prevent SQL injection
* Triggers provide audit logging for TrailLog

---

## Notes

* Fully modular and extendable
* Designed for academic use (MAL2018 module)

---

## License

This project is for **academic purposes only** and is **not intended for commercial use**

