# 📱 SJMobiles — Mobile Repair Shop Management System

A full-stack web application built with Django and MySQL to manage mobile repair shop operations — from logging repair requests to notifying customers via WhatsApp automatically.

---

## 🚀 Features

- 📋 **Repair Entry Form** — Admin can log device details (Phone Model, IMEI, Password, Complaint, Price) and customer info (Name, Phone Number)
- 🗄️ **MySQL Backend** — All repair data is securely stored in a MySQL database
- 📊 **Repair Dashboard** — View all repair entries in a clean, organized table
- ✅ **Complete Button** — Marks repair as completed and sends a WhatsApp message to the customer with the repair amount
- 🔴 **Return Button** — Marks repair as returned and notifies the customer that the phone could not be repaired
- 💬 **WhatsApp Notifications** — Automated messages sent via `pywhatkit`

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Django |
| Database | MySQL |
| Frontend | HTML, CSS |
| WhatsApp Automation | pywhatkit |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Amal9539/mobileproject.git
cd mobileproject
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django mysqlclient pywhatkit
```

### 4. Configure MySQL Database

In `mobileproject/settings.py`, update the database settings:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the Server
```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

---

## 💬 WhatsApp Notification Setup

This project uses **pywhatkit** to send WhatsApp messages automatically.

> ⚠️ Requirements:
> - Your PC must be **logged into WhatsApp Web** (`web.whatsapp.com`) before clicking Complete/Return
> - Works best on **desktop/laptop**
> - Messages are sent **2 minutes** after clicking the button

### Message on Complete ✅
```
Hello [Customer Name], your mobile ([Phone Model]) repair is COMPLETED!
Amount to pay: ₹[Amount]. Thank you for choosing SJMobiles!
```

### Message on Return 🔴
```
Hello [Customer Name], unfortunately your mobile ([Phone Model]) could not be repaired.
Please collect your phone from SJMobiles. Sorry for the inconvenience.
```

---

## 📁 Project Structure

```
mobileproject/
│
├── mobileapp/               # Main Django app
│   ├── models.py            # Database models
│   ├── views.py             # Business logic & WhatsApp integration
│   ├── urls.py              # URL routing
│   └── templates/           # HTML templates
│
├── mobileproject/           # Django project settings
│   ├── settings.py
│   └── urls.py
│
├── manage.py
├── PyWhatKit_DB.txt         # pywhatkit log file
└── README.md
```

---

## 📌 URLs

| URL | Description |
|-----|-------------|
| `/` | Home Page |
| `/mobileproject/user_get/` | Repair Entry Form |
| `/mobileproject/user_view/` | Repair Dashboard |
| `/complete/<id>/` | Mark repair as Complete & send WhatsApp |
| `/return/<id>/` | Mark repair as Returned & send WhatsApp |

---

## 🙌 Author

**Amal** — [GitHub](https://github.com/Amal9539)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
