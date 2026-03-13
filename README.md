# WikiQuiz AI

WikiQuiz AI turns any Wikipedia article into an interactive quiz (questions + answers + explanations) and keeps a history of generated quizzes and your submissions.

## Tech stack

### Frontend
- **HTML5, CSS3**
- **Vanilla JavaScript**
- **Bootstrap 5** (via CDN) + **Bootstrap Icons**
- **Google Fonts (Inter)**

### Backend
- **Python**
- **FastAPI** (REST API + serves the static frontend)
- **Uvicorn** (ASGI server)
- **SQLAlchemy** (ORM)
- **Pydantic** (schemas/validation)
- **PostgreSQL or SQLite** (configurable via env; defaults to SQLite if not provided)
- **Mistral AI** (`mistralai`) for quiz + related topics generation (with a fallback mode if no API key)
- **Requests + BeautifulSoup4** for Wikipedia scraping

## Features
- **Paste Wikipedia URL → generate a fresh 5-question quiz**
- **Difficulty labels** (easy/medium/hard)
- **Instant scoring + correct answers + explanations**
- **Further reading / related topics**
- **Auth**: sign up, login, logout, and **guest mode**
- **History**: list quizzes, start any quiz again
- **Stores quiz submissions** (score/percentage)

## How to run locally

### Prerequisites
- **Python 3.10+** recommended
- (Optional) **PostgreSQL** if you don’t want SQLite
- (Optional) **Mistral API key** for best quiz quality

### Backend (API + serves the frontend)

```bash
cd "backend quiz_wikipedia/backend"
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Create `backend/.env` (you can start from `backend/.env.example`), then set at least:

```env
# Recommended (Postgres)
DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DB_NAME?sslmode=require

# Or use DB_TYPE-based config (falls back to SQLite if nothing is set)
DB_TYPE=sqlite

# LLM
MISTRAL_API_KEY=your_mistral_api_key_here
```

Run:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open:
- **App UI**: `http://localhost:8000/`
- **API docs**: `http://localhost:8000/docs`

### Frontend (optional standalone)
The UI is a static site in `frontend/`.

```bash
cd "backend quiz_wikipedia/frontend"
python -m http.server 5500
```

Then open `http://localhost:5500/` (make sure your frontend `script.js` points to the backend URL if needed).

## Screenshots

![Home / Generate](assets/screenshots/01-home-generate.png)
![Sign up](assets/screenshots/02-signup.png)
![Quiz questions](assets/screenshots/03-quiz-questions.png)
![Quiz results + explanations](assets/screenshots/04-quiz-results.png)
![History](assets/screenshots/05-history.png)

## Submit Your Screen Record link
- Add your screen recording link here: `<PASTE_LINK>`
