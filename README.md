# Yedidiah — Forex Mentorship Platform

Full-stack Django + PostgreSQL website with crypto payments.

---

## Project Structure

```
yedidiah/
├── backend/
│   ├── manage.py
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── apps/
│       ├── core/        → Homepage view
│       ├── users/       → Custom user model + dashboard
│       ├── mentorship/  → Application form
│       ├── payments/    → NOWPayments crypto integration
│       ├── contact/     → Contact form
│       └── api/         → REST API status
├── frontend/
│   ├── static/
│   │   ├── css/style.css
│   │   └── js/script.js
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── dashboard/
│       ├── mentorship/
│       ├── payments/
│       └── contact/
├── requirements.txt
└── .env.template
```

---

## Setup Instructions

### 1. Clone & install dependencies

```bash
cd yedidiah
pip install -r requirements.txt
```

### 2. Set up environment variables

```bash
cp .env.template .env
# Open .env and fill in your values
```

### 3. Set up PostgreSQL

```sql
CREATE DATABASE yedidiah_db;
CREATE USER your_db_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE yedidiah_db TO your_db_user;
```

### 4. Run migrations

```bash
cd backend
python manage.py makemigrations users mentorship payments contact
python manage.py migrate
```

### 5. Create superuser (admin panel access)

```bash
python manage.py createsuperuser
```

### 6. Collect static files

```bash
python manage.py collectstatic
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000

---

## Key URLs

| URL | Description |
|-----|-------------|
| / | Homepage |
| /admin/ | Admin panel (manage students, applications, payments) |
| /mentorship/apply/ | Student application form |
| /payments/checkout/ | Crypto payment page |
| /dashboard/ | Student dashboard |
| /contact/ | Contact form |
| /accounts/login/ | Login |
| /accounts/signup/ | Register |

---

## NOWPayments Setup

1. Sign up at https://nowpayments.io
2. Get your API key from the dashboard
3. Set your IPN secret key
4. Add both to your `.env` file

---

## Admin Panel

Visit `/admin/` with your superuser credentials to:
- View and manage student applications
- Approve / reject applications
- View payment history
- Activate/deactivate student accounts
- Read contact form messages
