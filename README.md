# 📝 Flask To-Do List App

This is a simple and clean **To-Do List web application** built with **Flask**, allowing users to add, view, update, and delete tasks in real-time. It runs on a lightweight SQLite database and uses HTML, CSS, and Python for a full-stack experience.

---

## 🚀 Features

- ✅ Add new tasks
- 🗑️ Delete existing tasks
- 🔄 Update tasks
- 📅 View when each task was added
- 💾 Stores data persistently using SQLite
- 📱 Clean, responsive interface (HTML + CSS)

---

## 🖥️ Technologies Used

- Python
- Flask
- SQLite (via SQLAlchemy)
- HTML5 / CSS3
- Jinja2 templating

---

## 🔧 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
   cd REPO-NAME
   
2. **Activate a virtual environment**
   ```bash
   python -m venv venv
   
   On Windows
   venv\Scripts\activate
   
   On Mac/Linux
   source venv/bin/activate

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Run the app**
   ```bash
   python app.py
   The app will run locally at:
   http://127.0.0.1:5000/


  **Folder Structure:**
  ```bash
  /todo-app/
  │
  ├── app.py              # Main Flask app
  ├── templates/          # HTML files (Jinja2)
  │   └── index.html
  ├── static/             # CSS or other static files
  │   └── styles.css
  ├── requirements.txt    # Python dependencies
  └── README.md           # Project info
  ```

Created by Laali Nembot as a foundational project to learn Flask, full-stack development, and Git/GitHub workflows

