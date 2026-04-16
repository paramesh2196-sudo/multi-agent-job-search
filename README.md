# Multi-Agent Job Search System

A Python-based multi-agent AI pipeline built with **CrewAI** that automates the complete job search preparation workflow — from resume analysis to job matching. Ships with both a **web UI (Streamlit)** and a **CLI demo**.

---

## Table of Contents
1. [What It Does](#what-it-does)
2. [Architecture](#architecture)
3. [How Each Agent Works](#how-each-agent-works)
4. [Project Structure](#project-structure)
5. [Setup on a New Laptop](#setup-on-a-new-laptop)
6. [Running the Project](#running-the-project)
7. [Testing](#testing)
8. [Troubleshooting](#troubleshooting)
9. [Tech Stack](#tech-stack)

---

## What It Does

Paste your resume → 3 specialized AI agents work in sequence:

1. **Resume Screening Agent** — scores your resume, finds weaknesses
2. **Resume Improvement Agent** — rewrites it with metrics & ATS keywords
3. **Job Search Agent** — recommends roles, companies, and salary ranges

Output is shown in the browser (Streamlit) or saved to `./output/` (CLI).

---

## Architecture

```
┌──────────────┐
│ Your Resume  │  (text file or paste in UI)
└──────┬───────┘
       │
       ▼
┌──────────────────────────────────┐
│ AGENT 1: Resume Screening        │
│   Role: HR Recruiter             │
│   Output: structured analysis    │
└──────┬───────────────────────────┘
       │  (context passed to next agent)
       ▼
┌──────────────────────────────────┐
│ AGENT 2: Resume Improvement      │
│   Role: Career Coach             │
│   Output: rewritten resume       │
└──────┬───────────────────────────┘
       │  (context passed to next agent)
       ▼
┌──────────────────────────────────┐
│ AGENT 3: Job Search Strategist   │
│   Role: Talent Acquisition       │
│   Output: jobs + companies       │
└──────┬───────────────────────────┘
       │
       ▼
   Final Report
   (output/*.txt files or UI tabs)
```

Agents run **sequentially** — each agent's output becomes context for the next via CrewAI's `context=[previous_task]` parameter.

---

## How Each Agent Works

### 1. Resume Screening Agent (`agents.py`)
- **Role:** HR Recruiter with 10+ years experience
- **Input:** Raw resume text
- **Process:**
  - Evaluates technical skills depth
  - Checks experience quality & quantification
  - Analyzes ATS compatibility
  - Identifies structural gaps
- **Output:** Structured 7-section report (score, strengths, weaknesses, missing elements)

### 2. Resume Improvement Agent (`agents.py`)
- **Role:** Professional resume writer & career coach
- **Input:** Original resume + Agent 1's screening report
- **Process:**
  - Fixes identified weaknesses
  - Adds quantified achievements (numbers, %, metrics)
  - Rewrites bullets with strong action verbs
  - Adds Professional Summary section
  - Optimizes for ATS keywords
- **Output:** Complete rewritten ATS-optimized resume + top 5 changes list

### 3. Job Search Agent (`agents.py`)
- **Role:** Talent acquisition specialist & career consultant
- **Input:** Improved resume from Agent 2
- **Process:**
  - Maps profile to suitable job roles
  - Identifies target companies by tier
  - Provides salary ranges for each experience level
  - Recommends job platforms & application strategy
- **Output:** Job search strategy with roles, companies, salary info, action items

### Task Chaining (`tasks.py`)
CrewAI's `Task` objects pass context between agents:
```python
improvement_task = create_improvement_task(
    agent, resume_text,
    screening_task   # <-- this makes Agent 2 see Agent 1's output
)
```

### Crew Assembly (`crew.py`)
The `Crew` orchestrates agents in sequential `Process` mode:
```python
crew = Crew(
    agents=[screening_agent, improvement_agent, job_search_agent],
    tasks=[screening_task, improvement_task, job_search_task],
    process=Process.sequential,
)
```

---

## Project Structure

```
multi_agent_job_search/
├── app.py              # Streamlit web UI (demo mode, no API key)
├── demo.py             # CLI demo (no API key required)
├── main.py             # Production entry point (uses real OpenAI)
├── agents.py           # 3 CrewAI agent definitions
├── tasks.py            # 3 task definitions with context chaining
├── crew.py             # Crew assembly & execution
├── sample_resume.txt   # Sample input for testing
├── test_edge_cases.py  # 38 automated tests
├── requirements.txt    # Python dependencies
├── .env.example        # Template for API keys
├── .gitignore          # Excludes .env, output/, __pycache__
└── README.md           # This file
```

---

## Setup on a New Laptop

### Prerequisites
- **Python 3.10+** — [download here](https://www.python.org/downloads/)
- **Git** — [download here](https://git-scm.com/downloads)
- A terminal (Command Prompt / PowerShell on Windows, Terminal on macOS/Linux)

### Step 1 — Clone the repository
```bash
git clone https://github.com/paramesh2196-sudo/multi-agent-job-search.git
cd multi-agent-job-search
```

### Step 2 — Create a virtual environment (recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```
Or if you only want **demo mode** (lighter install):
```bash
pip install streamlit python-dotenv
```

### Step 4 — (Optional) Configure API key for real-AI mode
Only needed if you want to run `main.py` with real OpenAI calls.
```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```
Open `.env` in a text editor and replace `your_openai_api_key_here` with your actual OpenAI key (get one from https://platform.openai.com/api-keys).

### Step 5 — Verify the install
```bash
python -X utf8 test_edge_cases.py
```
You should see **`PASSED: 38 / 38`** at the bottom.

---

## Running the Project

### Option A — Web UI (Recommended for Presentations)
```bash
streamlit run app.py
```
Opens automatically in your browser at **http://localhost:8501**.

Features:
- Paste or use the sample resume
- Click **Run Agent Pipeline**
- Watch each agent work with live progress bars
- Download the improved resume as a file
- No API key required — uses demo outputs

### Option B — CLI Demo
```bash
python -X utf8 demo.py
```
Prints all 3 agent outputs to the terminal and saves them to `./output/`.

### Option C — Real AI (requires OpenAI key)
```bash
python main.py                              # uses sample_resume.txt
python main.py --resume path/to/cv.txt      # uses your own resume
```
Makes real API calls to OpenAI — typically costs $0.01–$0.05 per run.

### Output Files
After running `demo.py` or `main.py`, check `./output/`:
- `1_screening_report.txt` — Agent 1's analysis
- `2_improved_resume.txt` — Agent 2's rewrite
- `3_job_recommendations.txt` — Agent 3's job strategy

---

## Testing

Run the edge-case test suite:
```bash
python -X utf8 test_edge_cases.py
```
Expected: **38 / 38 PASSED**

Tests cover:
- File reading (valid, missing, empty, UTF-8, whitespace)
- Output saving (file creation, non-empty, idempotent)
- Agent & task factory functions
- Output integrity (required sections present)
- App.py syntax validity

---

## Troubleshooting

### UnicodeEncodeError on Windows
Run Python with UTF-8 flag:
```bash
python -X utf8 demo.py
```

### `ModuleNotFoundError: No module named 'crewai'`
Make sure your virtual environment is activated, then:
```bash
pip install -r requirements.txt
```

### `OPENAI_API_KEY not set` (when running `main.py`)
You're trying to run real-AI mode. Either:
- Add your key to `.env`, OR
- Use `python demo.py` instead (no key needed)

### Streamlit port already in use
```bash
streamlit run app.py --server.port 8504
```

### Pushed to wrong GitHub account
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/multi-agent-job-search.git
git push
```

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Agent Framework | **CrewAI** 0.28.8 |
| LLM | **OpenAI GPT-3.5-turbo** (via LangChain) |
| Web UI | **Streamlit** 1.35.0 |
| Language | **Python 3.10+** |
| Config | python-dotenv |
| Testing | Custom test runner (no external deps) |

---

## License

MIT — feel free to use for learning, college projects, or real job hunts.
