📝 Task Manager API

A RESTful Task Management API built using Django and Django REST Framework. This project allows users to manage tasks with authentication, filtering, and analytics features.

🚀 Features

User Authentication (JWT-based login & register)

Create, Read, Update, Delete (CRUD) Tasks

Task Prioritization (High, Medium, Low)

Task Status Tracking (Pending, Ongoing, Completed)

Filter tasks by priority and status

User-specific task access (secure endpoints)

Basic analytics (task count by status)

🛠 Tech Stack

Python

Django

Django REST Framework

SQLite (can be switched to PostgreSQL)

JWT Authentication

📂 API Endpoints
🔐 Authentication

POST /api/register/ → Register user

POST /api/login/ → Get access & refresh token

📋 Tasks

GET /api/tasks/ → Get all tasks

POST /api/tasks/ → Create task

GET /api/tasks/<id>/ → Get single task

PUT /api/tasks/<id>/ → Update task

DELETE /api/tasks/<id>/ → Delete task

📊 Analytics

GET /api/tasks/analytics/ → Task count by status
