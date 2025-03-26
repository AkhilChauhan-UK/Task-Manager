# Task Management API

This is a Django REST Framework-based API for managing tasks. It allows users to create tasks, assign them to users, and retrieve tasks assigned to specific users.

## Features
- Create a task
- Assign a task to one or multiple users
- Retrieve tasks assigned to a user

---

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip (Python package manager)
- PostgreSQL or SQLite (default)

### Installation Steps

1. **Run migrations**
   ```sh
   python manage.py migrate
   ```

2. **Create a superuser** (for Django Admin Panel)
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to set up admin credentials.

3. **Start the development server**
   ```sh
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/`

---

## API Endpoints

### **1. Create a Task**
- **Endpoint:** `POST /tasks/create/`
- **Request Body (JSON):**
  ```json
  {
    "name": "Fix Backend Bug",
    "description": "Resolve the issue in API response handling."
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "name": "Fix Backend Bug",
    "description": "Resolve the issue in API response handling.",
    "created_at": "2025-03-26T12:00:00Z",
    "status": "Pending"
  }
  ```

### **2. Assign a Task to a User**
- **Endpoint:** `PUT /tasks/{task_id}/assign/`
- **Request Body (JSON):**
  ```json
  {
    "assigned_users": [1, 2]
  }
  ```
- **Response:**
  ```json
  {
    "message": "Task assigned successfully!",
    "task": {
      "id": 1,
      "name": "Fix Backend Bug",
      "assigned_users": [1, 2]
    }
  }
  ```

### **3. Retrieve Tasks for a User**
- **Endpoint:** `GET /tasks/user/{user_id}/`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "name": "Fix Backend Bug",
      "description": "Resolve the issue in API response handling."
    }
  ]
  ```

---

## Test Credentials
- **Admin Panel:** `http://127.0.0.1:8000/admin/`
- **Username:** `admin`
- **Password:** `admin123` (or my created superuser credentials)

---

