# 🛠️ Django Task Manager API

## 🚀 Project Description
The **Django Task Manager API** is a RESTful service that allows you to:
- Create tasks
- Assign tasks to multiple users
- Retrieve tasks assigned to specific users
- Perform CRUD operations on tasks

---

## ⚙️ Tech Stack
- **Backend:** Django, Django REST Framework (DRF)
- **Database:** SQLite (default for development)
- **API Testing:** Postman / cURL
- **Python Version:** 3.x

---

## 🔥 Features
- ✅ Create tasks with a name, description, type, and status  
- ✅ Assign multiple users to a task  
- ✅ Retrieve tasks assigned to specific users  
- ✅ Update and delete tasks  
- ✅ Simple and clean Django REST API architecture  

---

## ⚙️ Installation and Setup

### ✅ Clone the Repository
```bash
git clone https://github.com/cseazeem/django-task-manager
cd django-task-manager


✅ Create a Virtual Environment

python3 -m venv venv           # For Linux/Mac
venv\Scripts\activate          # For Windows
source venv/bin/activate       # For Linux/Mac

✅ Install Dependencies

pip install -r requirements.txt

✅ Apply Migrations

python manage.py makemigrations
python manage.py migrate

✅ Run the Server

python manage.py runserver

📍 http://127.0.0.1:8000

🔥 API Endpoints
🛠️ 1. Create a Task
Endpoint: POST /api/tasks/

Request Body:
{
    "name": "Backend Development",
    "description": "Develop APIs using Django",
    "task_type": "Development",
    "status": "in_progress"
}

Response:
{
    "id": 1,
    "name": "Backend Development",
    "description": "Develop APIs using Django",
    "created_at": "2025-03-26T10:30:00Z",
    "completed_at": null,
    "task_type": "Development",
    "status": "in_progress",
    "assigned_users": []
}

🛠️ 2. Assign a Task to Users
Endpoint: POST /api/tasks/<task_id>/assign/

Request Body:
{
    "user_ids": [1, 2]
}

Response:
{
    "message": "Task assigned successfully"
}

🛠️ 3. Get Tasks for a Specific User
Endpoint: GET /api/user/<user_id>/tasks/

Response:
[
    {
        "id": 1,
        "name": "Backend Development",
        "description": "Develop APIs using Django",
        "created_at": "2025-03-26T10:30:00Z",
        "completed_at": null,
        "task_type": "Development",
        "status": "in_progress",
        "assigned_users": [
            {
                "id": 1,
                "username": "john_doe",
                "email": "john@example.com"
            }
        ]
    }
]

🛠️ 4. Get All Tasks
Endpoint: GET /api/tasks/

Response:
[
    {
        "id": 1,
        "name": "Backend Development",
        "description": "Develop APIs using Django",
        "created_at": "2025-03-26T10:30:00Z",
        "completed_at": null,
        "task_type": "Development",
        "status": "in_progress",
        "assigned_users": []
    },
    {
        "id": 2,
        "name": "UI Design",
        "description": "Create frontend screens",
        "created_at": "2025-03-26T11:00:00Z",
        "completed_at": null,
        "task_type": "Design",
        "status": "pending",
        "assigned_users": []
    }
]

🛠️ 5. Update a Task
Endpoint: PUT /api/tasks/<task_id>/

Request Body:
{
    "name": "Updated Task",
    "description": "Updated description",
    "task_type": "Testing",
    "status": "completed"
}

Response:
{
    "id": 1,
    "name": "Updated Task",
    "description": "Updated description",
    "created_at": "2025-03-26T10:30:00Z",
    "completed_at": "2025-03-27T12:00:00Z",
    "task_type": "Testing",
    "status": "completed",
    "assigned_users": []
}

🛠️ 6. Delete a Task
Endpoint: DELETE /api/tasks/<task_id>/

Response:
{
    "message": "Task deleted successfully"
}

✅ Author
👤 Mohd Azeen
📧 your.cseazeem@gmail.com
📍 GitHub: [Your GitHub Profile](https://github.com/cseazeem)
