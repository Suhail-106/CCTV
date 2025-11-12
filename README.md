
# CCTV projects

A Django-based website with user authentication, OTP verification, Tailwind integration, and secure email handling, and profile making with editing.

---

## 🚀 Prerequisites

* **Python 3.8+**
* **Node.js & npm** (for Tailwind CSS)
* **Git**

---

## 📥 1. Clone the Repository

```bash
git clone https://github.com/Suhail-106/amazone-clone.git
cd amazone-clone
```

---

## 🛡️ 2. Create & Activate Virtual Environment

```bash
python -m venv venv
```

### Activate (Windows):

```bash
venv\Scripts\activate
```

---

## 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ 4. Apply Migrations (Database Setup)

```bash
python manage.py migrate
```

---

## 🖥️ 5. Run the Project

### Terminal 1 – Start Django Server

```bash
python manage.py runserver

#### and after that tailwind and django both run with this command
```
npm run dev
```

Access Project at: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## ✉️ Email & OTP Configuration (Important)

> 🔐 **Do NOT hardcode your email or password!**

### Step 1 – Generate App Password (Google Account)

### Step 2 – Set Environment Variables

#### Windows (CMD/PowerShell):

```bash
set EMAIL_USER="your_email@gmail.com" in settings.py of folder name CCTV root line Numbser 145
set EMAIL_PASS="your_app_password" in settings.py of folder name CCTV root line Numbser 146
```

#### Linux/macOS (Bash/Zsh):

```bash
export EMAIL_USER="your_email@gmail.com"
export EMAIL_PASS="your_app_password"
```

### Step 3 – Set Email in `views.py`

Go to `uploadimage` → Function `login_view` → Line **103** → Add your email. For otp   
and Go to `uploadimage` -> Function `formfilling` -> **196** and same work in line **203** -> Add you email. For user information to your mail,and giving conformation to user.
last step Got to `uploadimage -> Funciton `formfilliing -> **197** -> Add your personal mail for take a work information to user.

---

## 🔑 Django Admin Credentials

```
Username: adminarbiya
Password: arbiya123
```

---

## 🧪 Test & Use

* Register/Login users
* OTP verification
* Product browsing (if included)
* Profile making with Editing

---

## 🤝 Acknowledgements

Thanks for using this project! Contributions and feedback are welcome.

---

## 🧑‍💻 Author

**Suhail** – Passionate Python & Django Developer
