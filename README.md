# 📚 BookHive — Digital Bookstore# 📚 BookHive — Role-Based Digital Bookstore Platform



A Django web application where admins upload books and users download them based on access permissions.<div align="center">



## What It Does![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)

![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)

- **Admins** upload books (PDFs) and approve access requests![DRF](https://img.shields.io/badge/DRF-3.14-ff1709?style=for-the-badge&logo=django&logoColor=white)

- **Users** browse, search, and download books![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

- **Free books** → anyone can download![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

- **Restricted books** → need admin approval

**A production-ready digital bookstore with secure file management and role-based access control**

## Features

[Features](#-features) • [Demo](#-live-demo) • [Installation](#-installation) • [Tech Stack](#-tech-stack) • [Screenshots](#-screenshots)

✅ User registration & login  

✅ Admin panel for book management  </div>

✅ Access request & approval workflow  

✅ Secure PDF downloads (permission-checked)  ---

✅ Search & filter by category/access type  

✅ User dashboard showing requests  ## 🎯 Project Overview

✅ REST API endpoints

BookHive is a full-stack web application that enables **admins** to upload and manage digital books (PDFs) while allowing **users** to browse, search, and download content based on permissions. The platform implements a sophisticated access control system where:

## Quick Start

- 📖 **Free Books** — Available to all authenticated users

```bash- 🔒 **Restricted Books** — Require admin approval before download

# 1. Create virtual environment- 👤 **Role-Based Access** — Admin and User roles with distinct permissions

python3 -m venv .venv- 🔐 **Secure File Serving** — PDFs served through permission-checked views, not direct URLs

source .venv/bin/activate

### Why BookHive?

# 2. Install dependencies

pip install -r requirements.txtThis project demonstrates real-world software engineering practices:

- **Security-first design** with secure file serving and authentication

# 3. Setup database- **Workflow automation** with approval systems and status tracking

python manage.py makemigrations- **Clean architecture** using Django's MVT pattern

python manage.py migrate- **RESTful API** for potential mobile/frontend integration

- **Production-ready** with Docker support and proper error handling

# 4. Load sample data (20 books + demo users)

python manage.py seed_bookhive---



# 5. Run server## ✨ Key Features

python manage.py runserver

```### 🔐 Authentication & Authorization

- ✅ User registration with email validation

**Open:** http://127.0.0.1:8000/- ✅ Secure login/logout with Django's built-in auth

- ✅ Role-based permissions (Admin vs User)

## Demo Accounts- ✅ Password reset functionality

- ✅ Session management

Created by seed command:

### 📚 Book Management

- **Admin**: `admin` / `admin1234`- ✅ Admin CRUD operations for books

- **User**: `demouser` / `demo1234`- ✅ PDF file upload with validation

- ✅ Cover image support (optional)

## Project Structure- ✅ Category/genre organization

- ✅ Access type control (Free/Restricted)

```- ✅ Bulk operations in admin panel

AYUSH/

├── store/              # Main app### 🔒 Access Control System

│   ├── models.py       # Book, Category, AccessRequest- ✅ **Free Books** — Instant download for authenticated users

│   ├── views.py        # Secure download & access logic- ✅ **Restricted Books** — Request → Admin Review → Approval → Download

│   ├── admin.py        # Admin customization- ✅ User dashboard to track access requests (Pending/Approved/Denied)

│   └── urls.py         # URL routing- ✅ Admin bulk approve/deny actions

├── templates/          # HTML templates- ✅ Duplicate request prevention (DB constraint)

├── static/css/         # Styles- ✅ Secure file serving with permission validation

├── media/books/        # Uploaded PDFs

└── manage.py### 🔍 Search & Discovery

```- ✅ Full-text search (title, author, description)

- ✅ Category-based filtering

## How It Works- ✅ Access type filters (Free/Restricted)

- ✅ Pagination for large datasets

### 1. Browse Books- ✅ Download count analytics

- Homepage shows all books with search and filters- ✅ Responsive card-based UI

- Cards show: title, author, category, Free/Restricted badge

### 🛠️ Technical Features

### 2. Download Free Book- ✅ Django ORM with optimized queries (`select_related`, `prefetch_related`)

- Click any Free book → Download button appears- ✅ Secure file serving (no direct URL access to PDFs)

- File downloads immediately- ✅ Download tracking and analytics

- ✅ REST API with Django REST Framework

### 3. Request Restricted Book- ✅ Custom management commands for seeding

- Click Restricted book → "Request Access" button- ✅ Docker & docker-compose support

- Submit request → goes to admin for approval- ✅ Production-ready settings structure



### 4. Admin Approves---

- Admin logs in → `/admin/store/accessrequest/`

- Select pending requests → Bulk action: "Approve"## 🚀 Quick Start



### 5. User Downloads### Prerequisites

- User refreshes book page → Download button now works- **Python 3.9+** installed

- File downloads after permission check- **pip** package manager

- **Git** (optional, for cloning)

## Key Tech Decisions

### Installation (Local Development)

**Secure File Serving**  

PDFs aren't served directly from `/media` URL. Every download goes through `download_book()` view which checks:```bash

1. User is logged in# 1. Clone or navigate to project

2. Book is Free OR user has approved AccessRequestcd /path/to/AYUSH



**Access Control Model**# 2. Create virtual environment

```pythonpython3 -m venv .venv

AccessRequest:

  user → book → status (pending/approved/denied)# 3. Activate virtual environment

  unique_together: (user, book)  # prevents duplicatessource .venv/bin/activate  # macOS/Linux

```# .venv\Scripts\activate   # Windows



**Admin Workflow**  # 4. Install dependencies

Bulk actions let admin approve/deny multiple requests at once. Saves reviewed_by and reviewed_at timestamps.pip install -r requirements.txt



## API Endpoints# 5. Apply database migrations

python manage.py migrate

- `GET /api/books/` — List all books (paginated)

- `GET /api/books/{id}/` — Book detail# 6. Load sample data (20 books, 8 categories, demo users)

- `GET /api/books/?search=python` — Search bookspython manage.py seed_bookhive



Example:# 7. (Optional) Create custom superuser

```bashpython manage.py createsuperuser

curl http://127.0.0.1:8000/api/books/

```# 8. Run development server

python manage.py runserver

## Demo Script (3 min)```



1. **Browse** (30s) → Show homepage, search, filters**Open in browser:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

2. **Free download** (20s) → Click free book, download works

3. **Restricted flow** (90s) → Request access as user → Switch to admin → Approve → Download works### 🔑 Default Login Credentials

4. **Dashboard** (20s) → Show user's requests and approved books

5. **API** (20s) → Show `/api/books/` endpoint| Role | Username | Password | Purpose |

|------|----------|----------|---------|

## Tech Stack| 👨‍💼 Admin | `admin` | `admin1234` | Full access, approve requests |

| 👤 User | `demouser` | `demo1234` | Browse and request books |

- **Backend**: Django 4.2, Django REST Framework

- **Database**: SQLite (dev), Postgres-ready> **Note:** These credentials are created by the `seed_bookhive` command.

- **Frontend**: Django Templates, CSS (responsive)

- **File Handling**: FileField with permission checks---

- **Auth**: Django built-in authentication

## 🐳 Docker Installation (Alternative)

## Future Enhancements

```bash

- [ ] Email notifications on approval# Build and start all services (web, db, redis)

- [ ] Chart.js analytics dashboarddocker compose up --build

- [ ] Unit tests for access control

- [ ] Book ratings & reviews# Access at http://localhost:8000

- [ ] Recommendations engine# Create superuser inside container

docker compose exec web python manage.py createsuperuser

## For Production```



- Switch to Postgres---

- Use S3/GCS for media files

- Use Nginx X-Sendfile for file serving## � Project Structure

- Enable HTTPS

- Set `DEBUG=False` and secure `SECRET_KEY````

📦 AYUSH/

---├── 📂 bookstore_project/          # Django project configuration

│   ├── settings.py                # Database, middleware, installed apps

**Built as a final-year project demonstrating Django, access control, and secure file handling.**│   ├── urls.py                    # Root URL routing

│   └── wsgi.py                    # WSGI application entry
│
├── 📂 store/                      # Main application
│   ├── 📄 models.py               # Book, Category, AccessRequest models
│   ├── 📄 views.py                # Business logic & view controllers
│   ├── 📄 admin.py                # Django admin customization
│   ├── 📄 serializers.py          # DRF serializers for API
│   ├── 📄 forms.py                # Registration & access request forms
│   ├── 📄 urls.py                 # App-level URL patterns
│   ├── 📄 urls_api.py             # REST API endpoints
│   ├── 📄 views_api.py            # API viewsets
│   │
│   ├── 📂 management/commands/
│   │   └── seed_bookhive.py       # Database seeding script
│   │
│   ├── 📂 migrations/             # Database migration files
│   └── 📂 templates/store/        # HTML templates (list, detail, dashboard)
│
├── 📂 templates/                  # Base templates
│   ├── base.html                  # Main layout with header/footer
│   └── registration/              # Login, register templates
│
├── 📂 static/                     # Static assets
│   └── css/styles.css             # Custom CSS (responsive, grid)
│
├── 📂 media/                      # User-uploaded files
│   └── books/
│       ├── pdfs/                  # Secure PDF storage
│       └── covers/                # Book cover images
│
├── 📄 manage.py                   # Django CLI tool
├── 📄 requirements.txt            # Python dependencies
├── 📄 Dockerfile                  # Docker image definition
├── 📄 docker-compose.yml          # Multi-container setup
├── 📄 entrypoint.sh               # Container startup script
└── 📄 README.md                   # This file
```

---

## 🎬 Live Demo Script (For Interviews)

### 📝 3-Minute Walkthrough

#### **Part 1: User Experience (60s)**
```
1. Open homepage: http://127.0.0.1:8000/
   → "Here's the landing page with 20 seeded books"
   → "Users can search by title/author, filter by category or access type"

2. Click a FREE book → Download immediately
   → "Free books are available to all authenticated users"
   → Shows download count incrementing

3. Click a RESTRICTED book
   → "Notice the 'Request Access' button instead of Download"
   → "This book requires admin approval"
```

#### **Part 2: Access Request Workflow (90s)**
```
4. Login as demouser (demouser / demo1234)
   → Navigate to restricted book
   → Click "Request Access" → Submit with optional message
   → "Request is now in PENDING state"

5. Open new tab → Login as admin (admin / admin1234)
   → Go to /admin/store/accessrequest/
   → Select pending request(s)
   → Actions dropdown → "Approve selected requests"
   → "Admin can bulk approve/deny with one click"

6. Back to demouser tab
   → Refresh book detail page
   → "Download button now appears — access granted!"
   → Download PDF successfully
```

#### **Part 3: Technical Deep Dive (30s)**
```
7. Show /dashboard/ → User's requests and download history
8. Open /api/books/ → DRF browsable API
9. Mention security:
   - "PDFs aren't served directly from /media/"
   - "Every download goes through permission check in views.py"
   - "download_book() validates: authenticated + (free OR approved)"
```

### 💡 Key Talking Points

| Feature | Technical Detail | Business Value |
|---------|-----------------|----------------|
| **Secure Downloads** | FileResponse with permission checks | Protects paid/premium content |
| **Approval Workflow** | Status state machine (pending→approved→download) | Enables content moderation |
| **Duplicate Prevention** | `unique_together` DB constraint | Data integrity |
| **Bulk Actions** | Django admin actions | Saves admin time |
| **Download Analytics** | Counter field + tracking | Business insights |

---

## 🖼️ Screenshots

### Homepage (Book Listing)
> Search, filters, pagination, and access badges

### Book Detail Page
> Download button (free) or Request Access button (restricted)

### User Dashboard
> Track access requests and view approved downloads

### Admin Panel
> Bulk approve/deny requests, manage books

> **Note:** Screenshots can be added by running the app and taking browser screenshots.

---

## 🏗️ Architecture & Technical Details

### 🔐 Security Implementation

```python
# Secure File Serving Pattern
@login_required
def download_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    # Permission validation
    can_download = False
    if book.access_type == 'free':
        can_download = True
    elif book.access_type == 'restricted':
        can_download = AccessRequest.objects.filter(
            user=request.user,
            book=book,
            status='approved'
        ).exists()
    
    if can_download:
        book.downloads += 1  # Analytics
        book.save()
        return FileResponse(open(book.pdf.path, 'rb'), as_attachment=True)
    
    return redirect('book_detail', pk=pk)  # Denied
```

**Why This Matters:**
- PDFs stored in `/media/` but **not accessible via direct URL**
- Every download requires authentication + permission check
- Files served through Django view, not web server (dev) or X-Sendfile (prod)

### 📊 Database Schema

```sql
-- Core Models
Category (id, name, slug)

Book (
    id, title, author, description,
    category_id FK → Category,
    pdf, cover,
    access_type ENUM('free', 'restricted'),
    downloads INT DEFAULT 0,
    created_at, updated_at
)

AccessRequest (
    id,
    user_id FK → User,
    book_id FK → Book,
    status ENUM('pending', 'approved', 'denied'),
    message TEXT,
    created_at, reviewed_at,
    reviewed_by_id FK → User,
    UNIQUE(user_id, book_id)  -- Prevent duplicates
)
```

**Key Relationships:**
- Book → Category (Many-to-One)
- AccessRequest → User (Many-to-One)
- AccessRequest → Book (Many-to-One)
- AccessRequest → Reviewer/Admin (Many-to-One, nullable)

### 🔄 Access Control Workflow

```mermaid
graph TD
    A[User clicks book] --> B{Access Type?}
    B -->|Free| C[Download Immediately]
    B -->|Restricted| D{Has Approved Request?}
    D -->|Yes| C
    D -->|No| E[Show 'Request Access' Button]
    E --> F[User submits request]
    F --> G[Status: PENDING]
    G --> H[Admin reviews in admin panel]
    H --> I{Admin Decision}
    I -->|Approve| J[Status: APPROVED]
    I -->|Deny| K[Status: DENIED]
    J --> C
    K --> L[User cannot download]
```

### ⚙️ Key Design Decisions

| Decision | Rationale | Trade-offs |
|----------|-----------|------------|
| **FileResponse in view** | Fine-grained permission control | Slower than direct Nginx serving (prod needs X-Sendfile) |
| **SQLite default** | Easy setup, portable | Not for high-concurrency prod (use PostgreSQL) |
| **unique_together constraint** | Prevents spam requests | Users can't re-request after denial (by design) |
| **Status enum field** | Clear state machine | No auto-expiry (could add with Celery) |
| **Separate API URLs** | Clean separation of concerns | Two URL config files to maintain |

---

## 🧪 Testing

### ✅ Manual Test Checklist

| Test Case | Expected Result | Status |
|-----------|----------------|--------|
| Anonymous user visits homepage | Can browse but no download buttons | ✅ |
| Anonymous user tries `/book/1/download/` | Redirect to login | ✅ |
| Logged-in user downloads free book | Immediate download, counter +1 | ✅ |
| Logged-in user views restricted book | Shows "Request Access" button | ✅ |
| User submits duplicate request | Error or info message (unique constraint) | ✅ |
| Admin approves request | Status changes to APPROVED | ✅ |
| Approved user downloads restricted book | Success, counter +1 | ✅ |
| Admin denies request | Status changes to DENIED, no download | ✅ |
| Search by title/author | Correct filtered results | ✅ |
| Filter by category | Only books in that category | ✅ |

### 🔬 Automated Tests (Future)

```bash
# Run tests (when implemented)
python manage.py test store

# Coverage report
coverage run --source='.' manage.py test
coverage report
```

**Test Coverage Goals:**
- Models: 80%+ (save, unique constraints, relationships)
- Views: 70%+ (permission checks, downloads, redirects)
- API: 80%+ (CRUD operations, search, filters)

---

## 🌐 API Documentation

### REST Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/books/` | List all books (paginated) | No |
| `GET` | `/api/books/{id}/` | Retrieve book detail | No |
| `GET` | `/api/books/?search=query` | Search books | No |
| `GET` | `/api/books/?access=free` | Filter by access type | No |
| `GET` | `/api/categories/` | List categories | No |

### Example API Calls

```bash
# List all books
curl http://127.0.0.1:8000/api/books/

# Search for Python books
curl "http://127.0.0.1:8000/api/books/?search=Python"

# Get specific book
curl http://127.0.0.1:8000/api/books/1/

# Filter free books
curl "http://127.0.0.1:8000/api/books/?access=free"
```

### Sample JSON Response

```json
{
    "count": 20,
    "next": "http://127.0.0.1:8000/api/books/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Python for Everyone",
            "author": "Guido van Rossum",
            "description": "Learn Python programming...",
            "category": 3,
            "category_name": "Programming",
            "cover": "/media/books/covers/python.jpg",
            "access_type": "free",
            "downloads": 45,
            "created_at": "2025-11-06T10:30:00Z"
        }
    ]
}
```

---

## 📊 Analytics & Metrics

### Current Tracking
- ✅ **Download counter** per book (incremented on each download)
- ✅ **Access request stats** (pending/approved/denied counts)
- ✅ **User activity dashboard** (requests history, approved books)

### Potential Enhancements

```python
# Future: Download logging
class DownloadLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    
# Admin dashboard with Chart.js
# - Top 10 most downloaded books (bar chart)
# - Downloads over time (line chart)
# - Request approval rate (pie chart)
# - Category popularity (donut chart)
```

---

## 🚀 Deployment

### 📦 Production Checklist

```bash
# 1. Environment variables (create .env file)
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:pass@host:5432/dbname

# 2. Database
# Switch from SQLite to PostgreSQL
pip install psycopg2-binary
# Update settings.py DATABASES config

# 3. Static & Media Files
python manage.py collectstatic --noinput
# Use S3/GCS for media in production

# 4. Web Server
pip install gunicorn
gunicorn bookstore_project.wsgi:application -w 4 -b 0.0.0.0:8000

# 5. Reverse Proxy (Nginx)
# Configure X-Sendfile for efficient file serving
```

### 🐳 Docker Deployment

```bash
# Production docker-compose
docker compose -f docker-compose.prod.yml up -d

# Check logs
docker compose logs -f web

# Run migrations in container
docker compose exec web python manage.py migrate

# Collect static files
docker compose exec web python manage.py collectstatic --noinput
```

### ☁️ Platform-Specific Guides

<details>
<summary><b>Heroku</b></summary>

```bash
# Install Heroku CLI and login
heroku login

# Create app
heroku create bookhive-app

# Add PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Set environment variables
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser
```
</details>

<details>
<summary><b>Railway / Render</b></summary>

1. Connect GitHub repository
2. Set environment variables in dashboard
3. Add build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
4. Add start command: `gunicorn bookstore_project.wsgi:application`
5. Deploy automatically on git push
</details>

<details>
<summary><b>AWS EC2 + RDS</b></summary>

```bash
# On EC2 instance
sudo apt update && sudo apt install python3-pip nginx -y
git clone https://github.com/yourusername/bookhive.git
cd bookhive
pip3 install -r requirements.txt

# Configure Nginx reverse proxy
# Set up Gunicorn as systemd service
# Use RDS PostgreSQL for database
# S3 for media files
```
</details>

### 🔒 Security Hardening

```python
# settings.py for production
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Use environment variables
import os
SECRET_KEY = os.environ.get('SECRET_KEY')
```

---

## 💻 Tech Stack

### Backend
- **Framework:** Django 4.2+ (Python 3.9+)
- **API:** Django REST Framework 3.14+
- **Database:** SQLite (dev), PostgreSQL (prod)
- **Server:** Gunicorn + Nginx
- **Authentication:** Django built-in auth

### Frontend
- **Template Engine:** Django Templates
- **Styling:** Custom CSS (Grid, Flexbox)
- **Icons:** Unicode emoji + potential integration with Font Awesome

### DevOps & Tools
- **Containerization:** Docker + docker-compose
- **Version Control:** Git
- **Package Management:** pip + venv
- **Production:** Gunicorn, Nginx, X-Sendfile

### Dependencies

```txt
Django>=4.2              # Web framework
djangorestframework>=3.14  # REST API
Pillow>=10.0             # Image processing
psycopg2-binary>=2.9     # PostgreSQL adapter
gunicorn>=20.1           # WSGI server
```

---

## 🎓 Learning Outcomes & Skills Demonstrated

### Technical Skills
- ✅ **Backend Development:** Django MVT architecture, ORM, middleware
- ✅ **Database Design:** Normalization, relationships, constraints, migrations
- ✅ **API Development:** RESTful design, DRF viewsets, serializers
- ✅ **Authentication:** User auth, permissions, role-based access
- ✅ **File Handling:** Secure uploads, permission-checked serving
- ✅ **Security:** CSRF, XSS protection, secure file access
- ✅ **DevOps:** Docker, environment variables, production config

### Software Engineering Practices
- ✅ **State Machines:** Access request workflow (pending→approved→download)
- ✅ **Data Integrity:** Unique constraints, foreign keys, validation
- ✅ **Admin Customization:** Bulk actions, filters, search
- ✅ **User Experience:** Responsive design, search, pagination
- ✅ **Documentation:** Comprehensive README, code comments

### Scalability Considerations
- Database indexing on frequently queried fields
- Query optimization with `select_related` and `prefetch_related`
- Pagination for large datasets
- Potential for caching layer (Redis)
- Async task queue with Celery (future)

---

## 🔮 Future Enhancements

### High Priority
- [ ] **Email Notifications:** Send email when access is approved (Django + SendGrid/SMTP)
- [ ] **Download Logging:** Track who downloaded what and when
- [ ] **Chart.js Dashboard:** Visual analytics for admin
- [ ] **Unit Tests:** Achieve 70%+ code coverage

### Medium Priority
- [ ] **Book Reviews & Ratings:** Users can rate and review books
- [ ] **Advanced Search:** Elasticsearch integration for full-text search
- [ ] **Recommendations:** "Users who downloaded X also downloaded Y"
- [ ] **Tags System:** ManyToMany relationship for book tags

### Nice-to-Have
- [ ] **Reading List:** Users can save books to read later
- [ ] **Social Features:** Share books, follow users
- [ ] **Mobile App:** React Native/Flutter app consuming the API
- [ ] **CI/CD Pipeline:** GitHub Actions for automated testing and deployment

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve BookHive:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines
- Follow PEP 8 style guide for Python code
- Add tests for new features
- Update documentation as needed
- Keep commits atomic and descriptive

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Sarthak Kumar Tiwari

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[Full MIT License text...]
```

---

## 👨‍💻 Author

**Sarthak Kumar Tiwari**
- Email: sarthak221711@gmail.com
- LinkedIn: [Add your LinkedIn]
- GitHub: [Add your GitHub]
- Portfolio: [Add your portfolio]

---

## 🙏 Acknowledgments

- Django Documentation Team
- Django REST Framework contributors
- Stack Overflow community
- Open-source contributors

---

## � Support

For questions, issues, or feedback:
- 📧 Email: sarthak221711@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/bookhive/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/bookhive/discussions)

---

<div align="center">

**⭐ Star this repo if you found it helpful!**

[![Made with Django](https://img.shields.io/badge/Made%20with-Django-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

**Built with ❤️ for learning and showcasing full-stack development skills**

</div>
# demo_project_book
