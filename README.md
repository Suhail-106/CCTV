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
<p>
  <h2>Image of my project layout for window screen</h2>
  <img src="https://github.com/user-attachments/assets/eb9dc20c-2359-4798-80b8-cfaf08d66d52" width="310">
  <img src="https://github.com/user-attachments/assets/786cb3c3-ef65-4a81-9a88-bae60a567c4e" width="310">
  <img src="https://github.com/user-attachments/assets/d7ab7d02-bc35-494b-a636-9d4fb1b22ede" width="310">
</p>

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

Go to `uploadimage` → Function `login_view` → Line **103** → Add your email. For otp,    
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

<p> 
  <h3>This is the image of mobile layott</h3>
  <h2>Image of my project layout for window screen</h2>
  <img src="https://github.com/user-attachments/assets/eb38409d-5e06-4e51-9e19-4a85779606a5" width="200">
  <img src="https://github.com/user-attachments/assets/32279829-6849-4d54-b1e9-7eba5d95b316" width="200">
  <img src="https://github.com/user-attachments/assets/18273096-bbf2-4c73-8694-3e96e2ef2ff6" width="200">
  <img width="200" src="https://github.com/user-attachments/assets/717dc819-67ac-4d69-bc4f-6251c1dc371a"/>
  <img width="200" src="https://github.com/user-attachments/assets/f794a461-aa23-4885-86cd-4710d152560c"/>
</p>

## 🧑‍💻 Author

**Suhail** – Passionate Python & Django Developer
