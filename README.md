# Multi-Agent Job Search System

A Python-based multi-agent pipeline built with **CrewAI** that automates the entire job search preparation process — from resume analysis to job matching.

## Architecture

```
Your Resume
    │
    ▼
┌─────────────────────────┐
│  Agent 1: Resume        │  Analyzes resume, scores it,
│  Screening Agent        │  finds strengths & weaknesses
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Agent 2: Resume        │  Rewrites resume with
│  Improvement Agent      │  metrics, action verbs, ATS fixes
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Agent 3: Job Search    │  Finds matching jobs,
│  Agent                  │  companies, salary info
└─────────────────────────┘
```

## Features

- **Resume Screening Agent** — scores resume (1–10), identifies strengths/weaknesses
- **Resume Improvement Agent** — rewrites resume to be ATS-friendly with quantified achievements
- **Job Search Agent** — recommends roles, companies, platforms, and application tips
- Sequential pipeline: each agent builds on the previous agent's output
- Outputs saved to `./output/` directory as text files
- **Demo mode** — works without any API key (great for presentations)

## Quick Start

### Demo Mode (No API key needed)
```bash
pip install -r requirements.txt
python demo.py
```

### Full Mode (OpenAI API key required)
```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
python main.py
python main.py --resume path/to/your_resume.txt
```

## Project Structure

```
multi_agent_job_search/
├── agents.py          # Agent definitions (roles, goals, backstories)
├── tasks.py           # Task definitions (chained pipeline)
├── crew.py            # CrewAI crew assembly
├── main.py            # Main entry point (real mode)
├── demo.py            # Demo mode (no API key needed)
├── sample_resume.txt  # Sample input resume
├── .env.example       # Environment variable template
├── requirements.txt   # Dependencies
└── output/            # Generated outputs (after running)
```

## Output Files

After running, the `output/` directory contains:
- `1_screening_report.txt` — Detailed resume analysis
- `2_improved_resume.txt` — Rewritten, ATS-optimized resume
- `3_job_recommendations.txt` — Curated job opportunities

## Tech Stack

| Component | Technology |
|-----------|------------|
| Agent Framework | CrewAI |
| LLM | OpenAI GPT-3.5-turbo |
| Language | Python 3.10+ |
| Config | python-dotenv |

## How It Works

1. The **Resume Screening Agent** reads your resume and produces a structured analysis covering technical skills, experience quality, ATS compatibility, and areas for improvement.

2. The **Resume Improvement Agent** takes the analysis and the original resume, then produces a fully rewritten version with quantified achievements, strong action verbs, and ATS keywords.

3. The **Job Search Agent** reads the improved profile and generates a complete job search strategy including target roles, companies, platforms, salary ranges, and actionable next steps.

Each agent communicates through CrewAI's task context system, ensuring outputs flow naturally through the pipeline.
