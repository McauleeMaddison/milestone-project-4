# milestone-project-4

# 🧊 Iced Insights — Full Stack Django E-Commerce Application

A full-featured, Stripe-powered e-commerce web application for selling **premium iced coffee trend data**. Built using **Django**, **Stripe**, **Allauth**, and modern development tools, this app allows users to authenticate, view both free and premium content, and securely purchase subscriptions.

> 💼 Built as a final milestone project for a Full Stack Frameworks (Django) course.

---

## 🚀 Live Demo

Coming soon — deploy via Heroku / Replit / Render.

---

## 📸 Screenshot

![Homepage Preview](static/img/screenshot-homepage.png)

---

## 🛠️ Tech Stack

| Layer         | Technology                                                                 |
|---------------|-----------------------------------------------------------------------------|
| **Backend**   | Python, Django (Django 5.x), SQLite                                         |
| **Frontend**  | HTML5, CSS3, PicoCSS, Django Templates                                      |
| **Auth**      | Django-Allauth (Registration/Login/Logout)                                 |
| **Payments**  | Stripe Checkout + Webhooks                                                  |
| **Deployment**| Replit / GitHub / Railway / Heroku-ready                                    |
| **Security**  | `.env`, CSRF protection, `.gitignore`, password hashing                     |

---

## 📦 Features

- ✅ User Registration & Login (via Allauth)
- ✅ Home page with high-quality product visuals
- ✅ Trends page (free and premium content)
- ✅ Stripe Checkout integration
- ✅ Stripe Webhooks to activate subscriptions
- ✅ Admin panel to manage users & trends
- ✅ Fully mobile-responsive layout
- ✅ Environment variable security using `python-dotenv`
- ✅ Separate free/premium content logic

---

## 📁 Project Structure

milestone-project-4/
├── dashboard/ # Core app with views, models, urls
├── icedinsights/ # Project settings and root urls
├── static/ # Static assets (CSS, JS, images)
├── templates/ # Custom Django templates
│ └── dashboard/
├── media/ # Uploaded content
├── .env # Secret environment variables
├── .gitignore
├── manage.py
└── requirements.txt