**TrailService Microservice**

**Overview**
TrailService is a Python-based microservice developed for the MAL2018 Information Management & Retrieval module. It provides CRUD operations for trail data, including names, descriptions, difficulty, GPS points, features, and photos. The microservice interacts with an external Authenticator API to validate users and ensures secure, structured data management.

**The service is built using:**
Python 3.12 with FastAPI
Microsoft SQL Server for persistent storage
Docker Desktop for containerized database
Azure Data Studio for database management
Swagger / OpenAPI for interactive API documentation

**Repository Structure**
TrailService/
│
├── app/                  # Python application code
│   ├── main.py           # FastAPI entry point
│   ├── database.py       # Database connection logic
│   ├── models.py         # Pydantic schemas
│   ├── crud.py           # CRUD operations
│   ├── routers.py        # API endpoints
│   └── utils.py          # Helper functions
│
├── sql/                  # Database scripts
│   ├── cw2_schema.sql    # Table creation
│   ├── procedures.sql    # Stored procedures
│   ├── trigger.sql       # Trigger for TrailLog
│   ├── views.sql         # Views for aggregated trail info
│   └── sample_data.sql   # Sample data for testing
│
├── requirements.txt      # Python dependencies
└── README.md             # This file

**Prerequisites**
Python 3.12
Docker Desktop (for SQL Server container)
Microsoft SQL Server 2022 image
Azure Data Studio (optional, for managing DB)

**Setup & Running**
**1. Start SQL Server**
Run SQL Server in Docker Desktop:

docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=YourPassword123" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2022-latest

Use Azure Data Studio or any SQL client to connect and run the scripts in /sql in the following order:
cw2_schema.sql
procedures.sql
trigger.sql
views.sql
sample_data.sql (optional)

**2. Install Python Dependencies**
pip install -r requirements.txt

**3. Run FastAPI Service**
From the project root:

**uvicorn app.main:app --reload**

The service will be available at:
**Base URL: http://127.0.0.1:8000
Swagger / OpenAPI docs: http://127.0.0.1:8000/docs**

**Testing the API**
Use Swagger UI or tools like Postman to test CRUD operations:
POST /trails – Create a new trail
GET /trails – Retrieve all trails
GET /trails/{id} – Retrieve a specific trail
PUT /trails/{id} – Update trail details
DELETE /trails/{id} – Delete a trail
All endpoints return JSON responses, and Pydantic validation ensures data integrity.

**Notes**
No sensitive data is stored; all user verification is via the external Authenticator API.
Parameterised queries and triggers ensure security and auditability.
The microservice is fully modular and extendable for additional functionality.

**License**
This project is for academic purposes (MAL2018 module) and is not intended for commercial use.
