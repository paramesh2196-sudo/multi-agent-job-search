"""
DEMO MODE — No API key required
================================
Runs the multi-agent pipeline with simulated agent outputs.
Perfect for college presentations and local testing.

Usage:
  python demo.py
  python demo.py --resume path/to/resume.txt
"""

import os
import argparse
import time
from pathlib import Path


SCREENING_REPORT = """
╔══════════════════════════════════════════════════════════╗
║           AGENT 1: RESUME SCREENING REPORT               ║
╚══════════════════════════════════════════════════════════╝

Overall Impression Score: 5.5 / 10

1. TECHNICAL SKILLS EVALUATION
   ✗ Skills listed are basic — no depth or proficiency levels stated
   ✗ Missing modern frameworks (Docker, REST APIs, Cloud)
   ✓ Core languages (Python, Java) are industry-relevant

2. EXPERIENCE & PROJECTS
   ✗ Internship description is vague ("helped in testing")
   ✗ No measurable outcomes or impact
   ✗ Only one project — insufficient for competitive market

3. EDUCATION
   ✓ Computer Science background is solid
   ✗ GPA 7.8 is decent but not highlighted well

4. FORMATTING & ATS COMPATIBILITY
   ✗ No professional summary section
   ✗ No keywords for ATS scanners
   ✗ Bullet points lack action verbs

5. KEY STRENGTHS
   ✓ Relevant educational background
   ✓ Python and Java are highly marketable
   ✓ Has internship experience

6. CRITICAL WEAKNESSES
   ✗ No quantified achievements (zero numbers/metrics)
   ✗ Vague project descriptions
   ✗ Missing: Summary, LinkedIn/GitHub impact, certifications depth

7. MISSING ELEMENTS
   - Professional Summary / Objective
   - Quantified impact metrics
   - Open source contributions
   - More projects (2-3 minimum)
   - Relevant coursework
"""

IMPROVED_RESUME = """
╔══════════════════════════════════════════════════════════╗
║         AGENT 2: ENHANCED RESUME OUTPUT                  ║
╚══════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JOHN DOE
📧 johndoe@email.com | 📞 +1-555-0100
🔗 linkedin.com/in/johndoe | 💻 github.com/johndoe
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROFESSIONAL SUMMARY
Motivated Computer Science graduate with hands-on experience in
full-stack development, database management, and software testing.
Skilled in Python, Java, and React with a proven ability to deliver
scalable web applications. Seeking a Software Developer / SDE-1 role
to contribute to impactful engineering teams.

TECHNICAL SKILLS
• Languages:    Python, Java, C++, JavaScript
• Web:          React.js, HTML5, CSS3, REST APIs
• Databases:    MySQL, SQLite
• Tools:        Git, GitHub, VS Code, Postman
• Concepts:     OOP, Data Structures, SDLC, Agile Basics

EDUCATION
B.Tech — Computer Science Engineering
XYZ University | 2020 – 2024 | CGPA: 7.8/10
Relevant Coursework: DSA, DBMS, OS, Web Technologies, Software Engineering

EXPERIENCE
Software Testing Intern | ABC Company | Jun 2023 – Aug 2023
• Automated 15+ test cases using Python scripts, reducing manual testing time by 30%
• Identified and documented 20+ bugs using JIRA, improving sprint resolution rate
• Collaborated with a 5-member dev team in an Agile environment

PROJECTS
Student Management System | Python, MySQL, Flask
• Developed a full-stack web application managing 200+ student records with CRUD operations
• Implemented secure login with session management, reducing unauthorized access to 0%
• Deployed locally serving 50+ concurrent users during demo

Expense Tracker App | Python, SQLite, Tkinter
• Built a desktop application to track monthly expenses with category-wise analysis
• Implemented data visualization charts, improving user financial awareness by 40%

CERTIFICATIONS
• Python for Everybody — University of Michigan, Coursera (2023)
• Introduction to Git & GitHub — Google, Coursera (2023)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOP 5 KEY CHANGES MADE:
1. Added Professional Summary — immediately grabs recruiter attention
2. Quantified all achievements with numbers/percentages
3. Used strong action verbs (Automated, Identified, Developed, Implemented)
4. Added a second project to demonstrate breadth of skills
5. Rewrote internship bullets to show measurable business impact
"""

JOB_RECOMMENDATIONS = """
╔══════════════════════════════════════════════════════════╗
║         AGENT 3: JOB SEARCH RECOMMENDATIONS              ║
╚══════════════════════════════════════════════════════════╝

RECOMMENDED JOB ROLES
  1. Junior Software Developer / SDE-1
  2. Python Developer (Entry Level)
  3. Full Stack Developer (Trainee)
  4. Associate Software Engineer
  5. Backend Developer (Junior)
  6. QA Automation Engineer
  7. Data Analyst (Entry Level)

TARGET COMPANIES TO APPLY
  Tier 1 (Stretch):       TCS, Infosys, Wipro, HCL, Cognizant
  Tier 2 (Good Fit):      Mphasis, LTIMindtree, Hexaware, Mastech
  Startups (High Growth): Razorpay, Zepto, Groww, Slice, Postman
  Product Companies:      Zoho, Freshworks, Chargebee, Browserstack
  Remote-Friendly:        Turing, Toptal, Remote.com listings

TOP JOB PLATFORMS
  🔍 LinkedIn Jobs     — linkedin.com/jobs (set job alerts daily)
  🔍 Naukri.com        — Upload updated resume, use "Freshers" filter
  🔍 Indeed India      — indeed.co.in
  🔍 Instahyre         — instahyre.com (AI-matched, great for freshers)
  🔍 Wellfound         — wellfound.com (startup-focused)
  🔍 Company Websites  — Apply directly on careers pages

SALARY EXPECTATIONS
  Fresher / 0-1 yr:    ₹3.5 – ₹6.5 LPA
  1-2 yrs experience:  ₹6 – ₹10 LPA
  With strong skills:  ₹8 – ₹15 LPA (product companies)

APPLICATION TIPS
  ✅ Customize cover letter for each company (2-3 sentences is enough)
  ✅ Reach out to 2nd-degree LinkedIn connections at target companies
  ✅ Apply within 24-48 hours of job posting for higher visibility
  ✅ Practice DSA on LeetCode (Easy/Medium) before interviews
  ✅ Build one more project on GitHub before applying to Tier 1

IMMEDIATE ACTION ITEMS (THIS WEEK)
  1. Upload the improved resume to Naukri and LinkedIn TODAY
  2. Complete 10 LeetCode Easy problems to warm up for coding rounds
  3. Send LinkedIn connection requests to 5 engineers at target companies
"""


def simulate_agent(agent_num: int, agent_name: str, delay: float = 1.5):
    print(f"\n{'-'*60}")
    print(f"  AGENT {agent_num}: {agent_name}")
    print(f"{'-'*60}")
    steps = ["Initializing...", "Processing inputs...", "Generating output...", "Complete ✓"]
    for step in steps:
        print(f"  [{agent_num}/{3}] {step}")
        time.sleep(delay / len(steps))


def read_resume(path: str) -> str:
    p = Path(path)
    if p.exists():
        return p.read_text(encoding="utf-8")
    return "Resume file not found — using default demo profile."


def save_results(output_dir: str = "output"):
    os.makedirs(output_dir, exist_ok=True)
    files = {
        "1_screening_report.txt": SCREENING_REPORT,
        "2_improved_resume.txt": IMPROVED_RESUME,
        "3_job_recommendations.txt": JOB_RECOMMENDATIONS,
    }
    for fname, content in files.items():
        with open(os.path.join(output_dir, fname), "w", encoding="utf-8") as f:
            f.write(content)


def main():
    parser = argparse.ArgumentParser(description="Multi-Agent Job Search Demo")
    parser.add_argument("--resume", default="sample_resume.txt", help="Path to resume file")
    args = parser.parse_args()

    print("\n" + "=" * 60)
    print("   MULTI-AGENT JOB SEARCH SYSTEM  [DEMO MODE]")
    print("   Built with CrewAI + Python")
    print("=" * 60)

    resume_text = read_resume(args.resume)
    print(f"\nResume loaded: {args.resume}")
    print(f"Characters: {len(resume_text)}")
    print("\nLaunching 3-agent pipeline...\n")

    simulate_agent(1, "Resume Screening Agent")
    print(SCREENING_REPORT)

    simulate_agent(2, "Resume Improvement Agent")
    print(IMPROVED_RESUME)

    simulate_agent(3, "Job Search Agent")
    print(JOB_RECOMMENDATIONS)

    print("\n" + "=" * 60)
    print("   PIPELINE COMPLETE")
    print("=" * 60)

    save_results()
    print("\nResults saved to ./output/ directory")
    print("\nTo run with real AI (requires OpenAI API key):")
    print("  cp .env.example .env   # add your key")
    print("  python main.py\n")


if __name__ == "__main__":
    main()
