"""
Multi-Agent Job Search System
==============================
Agents:
  1. Resume Screening Agent  - Analyzes and scores the resume
  2. Resume Improvement Agent - Rewrites and enhances the resume
  3. Job Search Agent        - Finds relevant job opportunities

Usage:
  python main.py                        # Uses sample_resume.txt
  python main.py --resume path/to/cv.txt
"""

import os
import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def read_resume(path: str) -> str:
    p = Path(path)
    if not p.exists():
        print(f"[ERROR] Resume file not found: {path}")
        sys.exit(1)
    return p.read_text(encoding="utf-8")


def save_results(results: dict, output_dir: str = "output"):
    os.makedirs(output_dir, exist_ok=True)
    files = {
        "1_screening_report.txt": results.get("screening_report", ""),
        "2_improved_resume.txt": results.get("improved_resume", ""),
        "3_job_recommendations.txt": results.get("job_recommendations", ""),
    }
    for fname, content in files.items():
        fpath = os.path.join(output_dir, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Saved: {fpath}")


def main():
    parser = argparse.ArgumentParser(description="Multi-Agent Job Search System")
    parser.add_argument(
        "--resume",
        type=str,
        default="sample_resume.txt",
        help="Path to resume text file (default: sample_resume.txt)",
    )
    args = parser.parse_args()

    # Validate API key
    if not os.getenv("OPENAI_API_KEY"):
        print("\n[ERROR] OPENAI_API_KEY not set.")
        print("Copy .env.example to .env and add your API key.\n")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("   MULTI-AGENT JOB SEARCH SYSTEM")
    print("=" * 60)
    print(f"\nReading resume from: {args.resume}")

    resume_text = read_resume(args.resume)
    print(f"Resume loaded ({len(resume_text)} characters)")

    print("\n[1/3] Starting Resume Screening Agent...")
    print("[2/3] Resume Improvement Agent will run next...")
    print("[3/3] Job Search Agent will run last...\n")

    from crew import run_job_search_crew

    results = run_job_search_crew(resume_text)

    print("\n" + "=" * 60)
    print("   PIPELINE COMPLETE — SAVING RESULTS")
    print("=" * 60)
    save_results(results)

    print("\n--- SCREENING REPORT PREVIEW ---")
    print(results["screening_report"][:500] + "..." if results["screening_report"] else "N/A")

    print("\n--- JOB RECOMMENDATIONS PREVIEW ---")
    print(results["job_recommendations"][:500] + "..." if results["job_recommendations"] else "N/A")

    print("\nAll outputs saved to ./output/ directory.")
    print("Done!\n")


if __name__ == "__main__":
    main()
