# SkillSwap

## Overview

SkillSwap is an AI-powered skill exchange platform that enables users to teach, learn, and collaborate with others through mentor matching, skill exchanges, community learning pods, and intelligent recommendations.

The platform connects learners and mentors based on skills, trust scores, reviews, and AI-driven recommendations to create a collaborative learning ecosystem.

---

## Features

### User Authentication

* User Registration
* JWT Authentication
* Secure Login
* User Profile Management

### Skill Management

* Add Skills to Teach
* Add Skills to Learn
* Skill Categorization
* Skill Search

### Smart Matching System

* Skill-Based Matching
* Match Suggestions
* Trust Score Ranking
* Activity-Based Ranking

### Exchange Requests

* Send Skill Exchange Requests
* Accept Requests
* Complete Sessions
* Request Tracking

### Reviews & Ratings

* User Reviews
* 1–5 Star Ratings
* Trust Score Calculation

### Credit Economy

* Earn Credits by Teaching
* Spend Credits by Learning
* Credit Transactions
* User Credit Tracking

### Community Pods

* Topic-Based Learning Communities
* Pod Memberships
* Weekly Challenges
* Challenge Submissions

### AI Features

#### AI Skill Description Generator

Generates beginner-friendly explanations for skills.

#### AI Skill Gap Analyzer

Analyzes a user's resume and career goals to identify:

* Current Skills
* Missing Skills
* Learning Roadmap

#### AI Mentor Recommendations

Provides recommendations for:

* Mentors
* Learning Pods
* Skills to Learn

#### Semantic Matching (Planned)

Matches related skills even when names differ.

Example:

* Python
* Django
* Flask
* FastAPI

---

## Tech Stack

### Backend

* Django
* Django REST Framework
* JWT Authentication
* SQLite (Development)
* PostgreSQL (Deployment)

### Frontend

* React
* Vite
* React Router
* Axios

### AI Integration

* Google Gemini API

### Deployment

* Neon PostgreSQL
* Render (Backend)
* Vercel (Frontend)

---

## Project Structure

```text
SkillSwap/
│
├── backend/
│   ├── accounts/
│   ├── skills/
│   ├── exchange/
│   ├── reviews/
│   ├── community/
│   ├── ai_features/
│   └── config/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── components/
│
└── README.md
```

---

## Trust Score Formula

Trust Score is calculated using:

Trust Score =
(Avg Rating × 0.6)

* (Completed Sessions × 0.3)
* (Activity Score × 0.1)

---

## Credit Economy

### Teaching

```text
Teach 1 Session
      ↓
Earn 10 Credits
```

### Learning

```text
Learn 1 Session
      ↓
Spend 10 Credits
```

---

## API Highlights

### Authentication

```http
POST /api/accounts/register/
POST /api/accounts/login/
GET  /api/accounts/profile/
```

### Skills

```http
GET /api/skills/search/
GET /api/skills/matches/
```

### Exchange Requests

```http
POST /api/exchange/send/
GET  /api/exchange/received/
GET  /api/exchange/sent/
POST /api/exchange/<id>/accept/
POST /api/exchange/<id>/complete/
```

### AI Features

```http
POST /api/ai/skill-description/
POST /api/ai/skill-gap/
POST /api/ai/mentor-recommendations/
```

---

## Future Enhancements

* Real-Time Chat
* Video Calling Integration
* AI Mentor Assistant
* Vector Embeddings
* Advanced Semantic Search
* Skill Certification System
* Leaderboards
* Notifications

---

## Author

Andrea Fernandes

Full Stack Developer | Django | React | AI Integration

---

## License

This project is developed for educational and learning purposes.
