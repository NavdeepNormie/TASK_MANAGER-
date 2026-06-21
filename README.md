# Task Tracker — Django

A multi-user task management web app built with Django. Users can sign up, log in, and manage their own tasks with priorities, due dates, and status filters.

---

## Features

- User authentication (signup, login, logout)
- Create, view, edit, and delete tasks
- Set priority (low / medium / high) and due date
- Mark tasks as complete
- Filter tasks by status and priority
- Each user only sees their own tasks

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (development) / PostgreSQL (production)
- **Templates:** Django templating engine
- **Auth:** Django's built-in authentication system

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/task-tracker.git
cd task-tracker

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser (optional, for admin access)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to use the app, or `http://127.0.0.1:8000/admin` for the admin panel.

## Project Structure

```
config/          # Project settings and root URL config
tasks/
  models.py      # Task model
  views.py       # All view functions
  forms.py       # TaskForm (ModelForm)
  urls.py        # App-level URL patterns
  admin.py       # Admin registration
  templates/
    tasks/       # All HTML templates
```

## Environment Variables

For production, set these as environment variables (do not hardcode in settings.py):

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | Set to `False` in production |
| `DATABASE_URL` | PostgreSQL connection string |
| `ALLOWED_HOSTS` | Comma-separated list of allowed domains |

## Running Tests

```bash
python manage.py test tasks
```

## License

MIT
