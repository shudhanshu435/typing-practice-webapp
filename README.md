# ⌨️ Typing Practice Web Application

A full-featured typing practice web application built using **Django**, **MySQL**, **HTML**, **CSS**, and **JavaScript**.  
The application allows users to practice typing, track their performance, view analytics, and compete with others through a leaderboard system.

---

# 🚀 Features

## 🔐 User Authentication

- User Registration with Full Name
- Login and Logout System
- Automatic User Profile Creation
- Secure authentication using Django built-in auth

---

## ⌨️ Typing Test System

- Random typing passage loading
- Difficulty selection:
  - Easy
  - Medium
  - Hard
- Timer-based typing test
- Custom time selection
- Manual test stop feature
- Character-by-character validation
- Error detection

---

## 📊 Performance Tracking

- Words Per Minute (WPM) calculation
- Accuracy calculation
- Error counting
- Automatic result saving
- User-specific typing history

---

## 📈 Dashboard Analytics

Interactive dashboard displaying:

- Total Tests
- Best WPM
- Average WPM
- Latest Accuracy

Charts implemented using:

- Chart.js
- WPM Progress Graph
- Accuracy Progress Graph
- WPM vs Date Graph

---

## 👤 User Profile System

Each user has:

- Full Name
- Username
- Email
- Date Joined
- Total Tests
- Best WPM
- Average WPM

---

## 🏆 Leaderboard System

- Displays Top Users
- Ranked by Best WPM
- Shows competitive performance ranking
- Highlights top performers

---

# 🛠️ Tech Stack

## Backend

- Python
- Django Framework

## Frontend

- HTML
- CSS
- Bootstrap
- JavaScript

## Database

- MySQL

## Visualization

- Chart.js

## Version Control

- Git
- GitHub

---

# ⚙️ Installation Guide

Follow these steps to run the project locally.

## Step 1 — Clone Repository


git clone https://github.com/your-username/typing-practice-webapp.git


## Step 2 — Navigate to Project


cd typing-practice-webapp


## Step 3 — Create Virtual Environment


python -m venv venv


## Step 4 — Activate Virtual Environment

Windows:


venv\Scripts\activate


Linux / Mac:


source venv/bin/activate


## Step 5 — Install Dependencies


pip install -r requirements.txt


## Step 6 — Run Migrations


python manage.py makemigrations   
python manage.py migrate


## Step 7 — Create Superuser


python manage.py createsuperuser


## Step 8 — Run Server


python manage.py runserver


Open browser:


http://127.0.0.1:8000/

---

# 🧠 Key Concepts Implemented

- Django Authentication System
- Django Signals
- AJAX Fetch API
- Database Relationships (ForeignKey, OneToOneField)
- Aggregation Functions (Avg, Max)
- Chart.js Integration
- Dynamic Template Rendering
- Bootstrap UI Design

---

# 👨‍💻 Author

**Shudhanshu Kumar**

Developed as part of hands-on Django learning and portfolio development.

