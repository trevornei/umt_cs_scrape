<<<<<<< HEAD
# umt_cs_scrape
I am scraping the course requirements for my B.S. of Computer Science at the University of Montana.
=======
#Welcome.
###My Name is Trevor Nei - I'm a CS student at the University of Montana. Here is my first full stack web app. The purpose of this app is to scrape my degrees course requirements, to save the tabular data to a GH repo, and for a web app hosted by GH Pages to show my degree progress.

#####About the Stack:

- **\*\***FE: Next.js
- **\*\***BE: Django & BS4

---

##What kind of data am I trying to extract?

### ()

---

# File Structure for the App.

umt_scrape/ # Root directory for your full-stack application
├── backend/ # Django backend
│ ├── cs_backend/ # Django project folder
│ │ ├── settings/ # Django project settings folder
│ │ │ ├── **init**.py
│ │ │ ├── asgi.py
│ │ │ ├── settings.py # Django project settings
│ │ │ ├── urls.py # Project-level URLs
│ │ │ ├── wsgi.py
│ │ │ └── ...
│ │ ├── courses/ # Django app for managing courses
│ │ │ ├── migrations/ # Database migration files
│ │ │ ├── **init**.py
│ │ │ ├── admin.py
│ │ │ ├── apps.py
│ │ │ ├── models.py # Course model
│ │ │ ├── serializers.py # API serializers for Django REST Framework
│ │ │ ├── urls.py # App-level URLs for courses
│ │ │ ├── views.py # API views
│ │ │ └── ...
│ │ ├── manage.py # Django CLI entry point
│ │ └── requirements.txt # Backend dependencies
│ └── cs_catalog/ # Scraping logic using BeautifulSoup
│ ├── main.py # Script to scrape and populate Django DB
│ └── ...
frontend/ # Next.js frontend
├── app/ # App Router main folder
│ ├── api/ # Backend API routes (if needed in the frontend)
│ │ ├── courses/ # Example API route for courses
│ │ │ ├── route.js # API logic for the 'courses' endpoint
│ │ └── ...
│ ├── courses/ # Folder for courses-related pages
│ │ ├── page.js # Main page for displaying courses
│ │ ├── [id]/ # Dynamic route for individual courses
│ │ │ ├── page.js # Individual course details
│ │ └── ...
│ ├── layout.js # Root layout file for the app
│ ├── page.js # Home page
│ ├── globals.css # Global styles (if using CSS)
│ └── ...
├── components/ # Reusable UI components
│ ├── CourseCard.js # Component for displaying course cards
│ ├── Navbar.js # Navigation bar
│ └── ...
├── public/ # Public assets (images, fonts, etc.)
│ ├── logo.png
│ └── ...
├── styles/ # Additional CSS modules or Tailwind files
│ ├── globals.css # Global styles
│ └── ...
├── package.json # Frontend dependencies
├── next.config.js # Next.js configuration
└── ...

---
>>>>>>> de02bd3 (First commit)
