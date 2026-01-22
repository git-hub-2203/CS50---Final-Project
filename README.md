# CS50---Final-Project
# Password Manager – Flask Web Application

## 📌 Overview

This project is a **simple web-based Password Manager** built with **Flask** and **SQLite**.
It allows users to securely store, view, update, and delete login credentials through a clean web interface.

The application was designed as a learning project to practice:

* Flask routing and templates
* CRUD operations
* SQLite database integration
* Basic session-based web application structure

---

## 🚀 Features

* Add new credentials (service, link, login, password, and notes)
* View all stored credentials in a single dashboard
* Update existing password entries
* Delete stored credentials
* Persistent storage using SQLite
* Simple and lightweight Flask architecture

---

## 🧱 Project Structure

```text
.
├── app.py              # Main Flask application
├── db.py               # Database helpers and queries
├── info.db            # SQLite database (created at runtime)
├── templates/
│   └── home.html       # Main interface template
├── static/
│   └── style.css       # Application styles (optional)
└── README.md           # Project documentation
```

---

## ⚙️ Technologies Used

* **Python 3**
* **Flask**
* **SQLite**
* **HTML / Jinja2**
* **CSS**

---

## 🗄️ Database Schema

The application uses a single table (`users`) with the following fields:

| Column   | Type | Description             |
| -------- | ---- | ----------------------- |
| link     | TEXT | Website or service URL  |
| name     | TEXT | Service or account name |
| login    | TEXT | Username or email       |
| password | TEXT | Stored password         |
| note     | TEXT | Optional notes          |

> ⚠️ **Note:** Passwords are currently stored in plaintext for educational purposes.

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone <repository-url>
cd password-manager
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

The application will be available at:

```
http://127.0.0.1:5000
```

---

## 🔐 Security Considerations

This project is **educational** and **not production-ready**.

To improve security in future versions:

* Hash passwords using Argon2 or bcrypt
* Add user authentication and sessions
* Encrypt sensitive fields
* Protect against SQL injection (parameterized queries everywhere)
* Use HTTPS and environment variables for secrets

---

## 📚 Educational Purpose

This project is ideal for:

* CS50 or introductory backend projects
* Learning Flask fundamentals
* Practicing database-driven web applications
* Understanding CRUD workflows

---

## 🛠️ Future Improvements

* User authentication system
* Password hashing and encryption
* Search and filter functionality
* Password strength checker
* Export/import credentials
* UI/UX improvements

---

## 📄 License

This project is open for educational and personal use.

