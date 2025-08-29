# GEMSTONE-CODING-ACADEMY
gemstone_academy/
│── gemstone_academy/         # Main project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
│── users/                    # Custom user model & roles
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py        # (for DRF APIs later)
│   ├── forms.py              # (for signup/login forms)
│
│── courses/                  # Coding courses
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│
│── enrollments/              # Student course enrollments
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── urls.py
│
│── projects/                 # Student project submissions
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── urls.py
│
│── payments/                 # Tuition, sponsorships, licensing
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── urls.py
│
│── marketing/                # Blog, demo days, social integration
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── urls.py
│
│── dashboard/                # Admin dashboards, analytics
│   ├── migrations/
│   ├── views.py
│   ├── urls.py
│
│── templates/                # Global templates
│   ├── base.html
│   ├── users/
│   ├── courses/
│   ├── dashboard/
│
│── static/                   # Static files (CSS, JS, Images)
│   ├── css/
│   ├── js/
│   ├── images/
│
│── manage.py