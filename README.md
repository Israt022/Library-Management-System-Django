
# 📖 BookHive BD - Library Management API

**BookHive BD** is a RESTful service built using Django and Django REST Framework (DRF). It allows librarians and members to manage books, borrow/return them, and view borrowing history, with proper authentication and role-based permissions.

---

## 🚀 Features

### 1. User Registration & Authentication
- JWT-based authentication using **Djoser** and **Simple JWT**.
- Secure endpoints for registration, login, token refresh, and token verification.
- Users are either **Librarians** or **Members**.

### 2. Role-Based Access Control
- **Librarians** can add, update, and delete books and users.
- **Members** can view books and borrow or return them.

### 3. Book Management
- CRUD operations for managing books.
- Each book includes: `title`, `author`, `ISBN`, `category`, and `availability`.

### 4. Borrowing System
- Members can borrow available books and return them when finished.
- System tracks borrow and return dates.

### 5. Member Management
- Members can view their own borrow history and profile.
- Librarians can manage member records.

### 6. API Documentation
- Auto-generated API docs using **Swagger (drf-yasg)**.
- Available in both Swagger UI and ReDoc format.

---

## 🛠 Technologies Used

- **Django** - Web framework
- **Django REST Framework (DRF)** - API development
- **Djoser + Simple JWT** - Authentication
- **drf-yasg** - API Documentation
- **PostgreSQL / SQLite** - Database

---

## ⚙️ Installation Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/bookhive-bd-api.git
cd bookhive-bd-api
```

2. **Create and activate virtual environment:**
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run migrations:**
```bash
python manage.py migrate
```

5. **Create a superuser:**
```bash
python manage.py createsuperuser
```

6. **Run the server:**
```bash
python manage.py runserver
```

---

## 📄 API Documentation

- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`

---

## 🔐 Environment Variables

Create a `.env` file with the following keys:
```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
EMAIL_HOST=your_email_host
```

---

## 💡 Future Enhancements

- Book reservation feature
- Email reminders for due dates
- Fine calculation for late returns
- Multi-library support with locations

---

## 🧑‍💻 Author
[Your Name](https://github.com/yourusername)

---

## 📄 License
This project is licensed under the MIT License.
