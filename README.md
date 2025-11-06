# 📝 FastAPI Blog API

A fully functional **Blog REST API** built using **FastAPI**, **SQLAlchemy**, and **JWT Authentication**.  
It allows users to **register, login, create blogs, comment, and manage their own posts** securely.

---

## 🚀 Features

 User Registration and Login (JWT Authentication)  
 Password Hashing using bcrypt  
 Create, Read, Delete Blogs  
 Add and Delete Comments on Blogs  
 Role-based Access Control (Users can delete only their own blogs/comments)  
 CORS Middleware for Frontend Integration  
 Secure JWT-based token validation  

---

## 🏗️ Tech Stack

| Layer | Technology |
|:------|:------------|
| Backend Framework | FastAPI |
| ORM | SQLAlchemy |
| Authentication | JWT (via python-jose) |
| Password Hashing | bcrypt |
| Database | SQLite (default, can be switched to MySQL/PostgreSQL) |
| Language | Python 3.10+ |

---

## 📂 Project Structure

```
FastAPI-Blog/
│
├── main.py                # Main application entry point
├── models.py              # SQLAlchemy models (User, Blog, Comment)
├── schemas.py             # Pydantic models for request/response validation
├── database.py            # Database setup and session handling
├── utils.py               # Token creation & password hashing utilities
├── dependencies.py        # Dependencies (get_db, get_current_user)
├── temp.txt               # Stores secret key or test data
└── requirements.txt       # Python dependencies
```

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/fastapi-blog.git
cd fastapi-blog
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate       # On macOS/Linux
venv\Scripts\activate        # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

Example `requirements.txt`:
```
fastapi
uvicorn
sqlalchemy
pydantic
python-jose
bcrypt
passlib[bcrypt]
```

### 4️⃣ Run the Server
```bash
uvicorn main:app --reload
```

Server will start at 👉  
`http://127.0.0.1:8000`

---

## 🔑 Authentication

All secured routes use **JWT Bearer Tokens**.

### Get a Token
POST `/login`  

curl -X POST "http://127.0.0.1:8000/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user1&password=pass@1234"

{"access_token":"eyJ...","token_type":"bearer"}


Body (Form Data):
```json
{
  "username": "user1",
  "password": "pass@1234"
}
```

Response:
```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

### Use in Authorization Header
```
Authorization: Bearer <JWT_TOKEN>
```

---

## 🧠 API Endpoints

### 👤 User Routes
| Method | Endpoint | Description |
|:-------|:----------|:-------------|
| POST | `/register` | Register new user |
| POST | `/login` | Login and get access token |
| DELETE | `/delete_account` | Delete your account (with password) |

---

### 📝 Blog Routes
| Method | Endpoint | Description |
|:-------|:----------|:-------------|
| GET | `/blogs` | Get all blogs |
| GET | `/blogs/{blog_id}` | Get single blog by ID |
| POST | `/blogs/new` | Create a new blog *(Authenticated)* |
| DELETE | `/blogs/{blog_id}` | Delete your own blog *(Authenticated)* |

---

### 💬 Comment Routes
| Method | Endpoint | Description |
|:-------|:----------|:-------------|
| GET | `/comments/{blog_id}` | Get comments for a blog |
| POST | `/comments` | Add a comment *(Authenticated)* |
| DELETE | `/comments/{comment_id}` | Delete your own comment *(Authenticated)* |

---

## 🧩 Example Users

You can register and test with:
| Username | Password |
|:----------|:----------|
| user1 | pass@1234 |
| user2 | pass@1234 |
| user3 | pass@1234 |

---

## 🧰 Environment Variables

Store your environment secrets in a `.env` or `temp.txt` file:

```
SECRET_KEY = "fee104a9e7ce7f80363ce1ea0a37a229d61f169136422a656a08ec447dacf422"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 100
```

---

## 🧪 Testing the API

You can test endpoints using:

- [Swagger UI](http://127.0.0.1:8000/docs)
- [Redoc UI](http://127.0.0.1:8000/redoc)
- Postman / Thunder Client

---

## 📜 License

This project is licensed under the **MIT License** — free to use and modify.

---

## 👨‍💻 Author

**Vishal Donda**  
🔗 GitHub: [@vishaldonda](https://github.com/vishaldonda)

---

**Enjoy building! 🚀**
