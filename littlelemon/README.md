# Little Lemon – Back-End Developer Capstone Project

A Django REST Framework API for the Little Lemon restaurant, built for the Meta Back-End Developer Professional Certificate capstone.

---

## Tech Stack

| Layer     | Technology                    |
|-----------|-------------------------------|
| Framework | Django 4.2                    |
| API       | Django REST Framework 3.14    |
| Auth      | Djoser + DRF Token Auth       |
| Database  | MySQL                         |
| Testing   | Django TestCase + DRF APIClient |

---

## API Paths (for peer review / Insomnia testing)

### 🔐 Authentication (Djoser)

| Method | Path                 | Description                   | Auth Required |
|--------|----------------------|-------------------------------|---------------|
| POST   | `/auth/users/`       | Register a new user           | No            |
| POST   | `/auth/token/login/` | Obtain auth token             | No            |
| POST   | `/auth/token/logout/`| Invalidate auth token         | Yes           |

### 🍽️ Menu API

| Method | Path               | Description           | Auth Required |
|--------|--------------------|-----------------------|---------------|
| GET    | `/api/menu/`       | List all menu items   | No            |
| POST   | `/api/menu/`       | Create a menu item    | Yes           |
| GET    | `/api/menu/<id>/`  | Retrieve single item  | No            |
| PUT    | `/api/menu/<id>/`  | Update a menu item    | Yes           |
| DELETE | `/api/menu/<id>/`  | Delete a menu item    | Yes           |

### 📅 Booking API

| Method | Path                    | Description              | Auth Required |
|--------|-------------------------|--------------------------|---------------|
| GET    | `/api/bookings/`        | List all bookings        | Yes           |
| POST   | `/api/bookings/`        | Create a booking         | Yes           |
| GET    | `/api/bookings/<id>/`   | Retrieve a booking       | Yes           |
| PUT    | `/api/bookings/<id>/`   | Update a booking         | Yes           |
| DELETE | `/api/bookings/<id>/`   | Delete a booking         | Yes           |

### 🌐 HTML Pages (Django static views)

| Path                      | Description        |
|---------------------------|--------------------|
| `/restaurant/`            | Home page          |
| `/restaurant/about/`      | About page         |
| `/restaurant/menu/`       | Menu listing       |
| `/restaurant/menu/<id>/`  | Menu item detail   |

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/littlelemon.git
cd littlelemon
```

### 2. Create & activate a virtual environment
```bash
python -m venv env
source env/bin/activate      # macOS/Linux
env\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Create the database:
```sql
CREATE DATABASE littlelemon;
CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'employee@123!';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'admindjango'@'localhost';
FLUSH PRIVILEGES;
```

### 5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```

### 8. Run unit tests
```bash
python manage.py test
```

---

## Testing with Insomnia

1. **Register a user:**  
   `POST http://127.0.0.1:8000/auth/users/`  
   Body: `{ "username": "testuser", "password": "testpass123", "email": "test@example.com" }`

2. **Get your token:**  
   `POST http://127.0.0.1:8000/auth/token/login/`  
   Body: `{ "username": "testuser", "password": "testpass123" }`

3. **Use the token in Insomnia:**  
   Set header: `Authorization: Token <your_token_here>`

4. **Test menu endpoints** (no auth needed for GET):  
   `GET http://127.0.0.1:8000/api/menu/`

5. **Test booking endpoints** (auth required):  
   `POST http://127.0.0.1:8000/api/bookings/`  
   Body: `{ "name": "John Doe", "no_of_guests": 4, "booking_date": "2024-08-15T19:00:00Z" }`
