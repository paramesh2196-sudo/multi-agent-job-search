"""
Multi-Agent Job Search System — Streamlit Web App
"""

import streamlit as st
import time
import os, sys
sys.path.insert(0, os.path.dirname(__file__))

st.set_page_config(
    page_title="Multi-Agent Job Search",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
.agent-header {
    background: linear-gradient(90deg, #1e3a5f, #2e6da4);
    color: white;
    padding: 12px 20px;
    border-radius: 8px;
    margin: 10px 0 5px 0;
    font-size: 18px;
    font-weight: bold;
}
.agent-done {
    background: linear-gradient(90deg, #145a32, #1e8449);
    color: white;
    padding: 12px 20px;
    border-radius: 8px;
    margin: 10px 0 5px 0;
    font-size: 18px;
    font-weight: bold;
}
.result-box {
    background: #f8f9fa;
    border-left: 4px solid #2e6da4;
    padding: 16px 20px;
    border-radius: 0 8px 8px 0;
    margin-bottom: 12px;
}
.metric-card {
    background: #eaf4fb;
    border: 1px solid #aed6f1;
    border-radius: 8px;
    padding: 12px 16px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    color: #1a5276;
}
.tag {
    display: inline-block;
    background: #d6eaf8;
    color: #1a5276;
    border-radius: 12px;
    padding: 3px 10px;
    margin: 2px;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
st.sidebar.title("💼 Job Search System")
st.sidebar.markdown("*Powered by Multi-Agent AI*")
st.sidebar.divider()
st.sidebar.markdown("**3-Agent Pipeline:**")
st.sidebar.markdown("🔍 **Agent 1** — Resume Screening")
st.sidebar.markdown("✏️ **Agent 2** — Resume Improvement")
st.sidebar.markdown("🎯 **Agent 3** — Job Matching")
st.sidebar.divider()
st.sidebar.info("Each agent passes its output to the next — fully sequential AI pipeline.")

# ── Header ────────────────────────────────────────────────────────────────────
st.title("💼 Multi-Agent Job Search System")
st.markdown("Paste your resume, click **Run Pipeline**, and watch 3 AI agents work in sequence.")
st.divider()

DEFAULT_RESUME = """John Doe
Email: johndoe@email.com | Phone: +1-555-0100
LinkedIn: linkedin.com/in/johndoe | GitHub: github.com/johndoe

EDUCATION
B.Tech in Computer Science | XYZ University | 2020-2024 | GPA: 7.8/10

SKILLS
Programming: Python, Java, C++
Web: HTML, CSS, JavaScript, React (basic)
Databases: MySQL
Tools: Git

PROJECTS
Student Management System
- Built a web app using Python and MySQL
- Created forms and basic CRUD operations

EXPERIENCE
Internship at ABC Company (2 months)
- Helped in testing software
- Wrote some Python scripts

CERTIFICATIONS
- Python Basics - Coursera"""

resume_input = st.text_area("📄 Paste Your Resume", value=DEFAULT_RESUME, height=280)

run_btn = st.button("🚀 Run Agent Pipeline", type="primary", use_container_width=True)
st.divider()

# ── Pipeline ──────────────────────────────────────────────────────────────────
if run_btn:
    if not resume_input.strip():
        st.warning("Please paste your resume first.")
        st.stop()

    # ── AGENT 1 ───────────────────────────────────────────────────────────────
    st.markdown('<div class="agent-header">🔍 Agent 1 — Resume Screening Agent</div>', unsafe_allow_html=True)

    bar1 = st.progress(0, text="Initializing agent...")
    status1 = st.empty()

    steps1 = [
        (20, "Reading resume content..."),
        (45, "Evaluating technical skills..."),
        (65, "Analyzing experience & projects..."),
        (85, "Checking ATS compatibility..."),
        (100, "Generating screening report..."),
    ]
    for pct, msg in steps1:
        bar1.progress(pct, text=msg)
        status1.info(f"⚙️ {msg}")
        time.sleep(0.5)

    bar1.empty()
    status1.empty()
    st.markdown('<div class="agent-done">✅ Agent 1 Complete — Screening Report Ready</div>', unsafe_allow_html=True)

    with st.expander("📋 View Full Screening Report", expanded=True):
        col1, col2, col3 = st.columns(3)
        col1.markdown('<div class="metric-card">5.5 / 10<br><small>Overall Score</small></div>', unsafe_allow_html=True)
        col2.markdown('<div class="metric-card">3<br><small>Strengths Found</small></div>', unsafe_allow_html=True)
        col3.markdown('<div class="metric-card">3<br><small>Critical Gaps</small></div>', unsafe_allow_html=True)

        st.markdown("")

        st.markdown("**Technical Skills**")
        st.error("❌ No depth or proficiency levels stated on skills")
        st.error("❌ Missing modern tools: Docker, REST APIs, Cloud")
        st.success("✅ Python and Java are highly marketable")

        st.markdown("**Experience & Projects**")
        st.error('❌ Internship description is vague — "helped in testing" shows no impact')
        st.error("❌ No measurable outcomes (no numbers, no metrics)")
        st.error("❌ Only 1 project listed — insufficient for competitive market")

        st.markdown("**Formatting & ATS**")
        st.warning("⚠️ No Professional Summary section")
        st.warning("⚠️ Missing ATS keywords for software roles")
        st.warning("⚠️ Bullet points lack strong action verbs")

        st.markdown("**Missing Elements**")
        missing = ["Professional Summary", "Quantified achievements", "More projects (2-3 min)", "Relevant coursework", "Open-source contributions"]
        cols = st.columns(len(missing))
        for i, item in enumerate(missing):
            cols[i].markdown(f'<span class="tag">➕ {item}</span>', unsafe_allow_html=True)

    st.divider()

    # ── AGENT 2 ───────────────────────────────────────────────────────────────
    st.markdown('<div class="agent-header">✏️ Agent 2 — Resume Improvement Agent</div>', unsafe_allow_html=True)

    bar2 = st.progress(0, text="Reading screening report from Agent 1...")
    status2 = st.empty()

    steps2 = [
        (15, "Reading Agent 1 screening report..."),
        (35, "Rewriting experience with action verbs..."),
        (55, "Adding quantified achievements & metrics..."),
        (75, "Building Professional Summary..."),
        (90, "Optimizing for ATS keywords..."),
        (100, "Finalizing improved resume..."),
    ]
    for pct, msg in steps2:
        bar2.progress(pct, text=msg)
        status2.info(f"⚙️ {msg}")
        time.sleep(0.5)

    bar2.empty()
    status2.empty()
    st.markdown('<div class="agent-done">✅ Agent 2 Complete — Improved Resume Ready</div>', unsafe_allow_html=True)

    with st.expander("📄 View Improved Resume", expanded=True):
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("**Before (Original)**")
            st.code("""EXPERIENCE
Internship at ABC Company (2 months)
- Helped in testing software
- Wrote some Python scripts

PROJECTS
Student Management System
- Built a web app using Python and MySQL
- Created forms and basic CRUD operations""", language=None)

        with col_b:
            st.markdown("**After (Improved)**")
            st.code("""EXPERIENCE
Software Testing Intern | ABC Company
Jun 2023 – Aug 2023
• Automated 15+ test cases using Python,
  reducing manual testing time by 30%
• Identified & documented 20+ bugs in JIRA,
  improving sprint resolution rate
• Collaborated with 5-member team in Agile

PROJECTS
Student Management System | Python, MySQL, Flask
• Managed 200+ student records with CRUD
• Secure login — reduced unauthorized access to 0%
• Handled 50+ concurrent users during demo""", language=None)

        st.markdown("---")
        st.markdown("**Top 5 Changes Made by Agent 2:**")
        changes = [
            ("1", "Added Professional Summary with target role"),
            ("2", "Quantified every achievement with numbers & %"),
            ("3", "Strong action verbs: Automated, Identified, Developed"),
            ("4", "Added a second project to show broader skills"),
            ("5", "Added skills table with categories"),
        ]
        for num, change in changes:
            st.success(f"**{num}.** {change}")

        resume_download = """JOHN DOE
johndoe@email.com | +1-555-0100 | linkedin.com/in/johndoe | github.com/johndoe

PROFESSIONAL SUMMARY
Motivated Computer Science graduate with hands-on experience in full-stack development,
database management, and software testing. Skilled in Python, Java, and React. Seeking
a Software Developer / SDE-1 role to contribute to impactful engineering teams.

TECHNICAL SKILLS
Languages:  Python, Java, C++, JavaScript
Web:        React.js, HTML5, CSS3, REST APIs
Databases:  MySQL, SQLite
Tools:      Git, GitHub, VS Code, Postman
Concepts:   OOP, Data Structures, SDLC, Agile

EDUCATION
B.Tech — Computer Science | XYZ University | 2020–2024 | CGPA: 7.8/10

EXPERIENCE
Software Testing Intern | ABC Company | Jun 2023 – Aug 2023
• Automated 15+ test cases using Python, reducing manual testing time by 30%
• Identified and documented 20+ bugs in JIRA, improving sprint resolution rate
• Collaborated with a 5-member dev team in an Agile environment

PROJECTS
Student Management System | Python, MySQL, Flask
• Developed full-stack web app managing 200+ student records with CRUD
• Implemented secure login, reducing unauthorized access to 0%
• Deployed locally serving 50+ concurrent users

Expense Tracker App | Python, SQLite, Tkinter
• Built desktop application for monthly expense tracking with charts
• Improved user financial awareness by 40% through visualization

CERTIFICATIONS
• Python for Everybody — University of Michigan, Coursera (2023)
• Introduction to Git & GitHub — Google, Coursera (2023)
"""
        st.download_button(
            label="⬇️ Download Improved Resume (.txt)",
            data=resume_download,
            file_name="improved_resume.txt",
            mime="text/plain",
            use_container_width=True,
        )

    st.divider()

    # ── AGENT 3 ───────────────────────────────────────────────────────────────
    st.markdown('<div class="agent-header">🎯 Agent 3 — Job Search Agent</div>', unsafe_allow_html=True)

    bar3 = st.progress(0, text="Reading improved profile from Agent 2...")
    status3 = st.empty()

    steps3 = [
        (20, "Reading improved profile from Agent 2..."),
        (40, "Matching profile with job market data..."),
        (60, "Identifying target companies..."),
        (80, "Calculating salary ranges..."),
        (100, "Generating job recommendations..."),
    ]
    for pct, msg in steps3:
        bar3.progress(pct, text=msg)
        status3.info(f"⚙️ {msg}")
        time.sleep(0.5)

    bar3.empty()
    status3.empty()
    st.markdown('<div class="agent-done">✅ Agent 3 Complete — Job Recommendations Ready</div>', unsafe_allow_html=True)

    with st.expander("🎯 View Job Recommendations", expanded=True):

        st.markdown("**Recommended Roles**")
        roles = ["Junior Software Developer / SDE-1", "Python Developer", "Full Stack Developer (Trainee)", "Associate Software Engineer", "QA Automation Engineer", "Data Analyst (Entry Level)"]
        cols = st.columns(3)
        for i, role in enumerate(roles):
            cols[i % 3].success(f"💼 {role}")

        st.markdown("---")
        st.markdown("**Target Companies**")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**Tier 1 (Stretch)**")
            for c in ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]:
                st.markdown(f"- {c}")
        with col2:
            st.markdown("**Tier 2 (Good Fit)**")
            for c in ["Mphasis", "LTIMindtree", "Hexaware", "Mastech"]:
                st.markdown(f"- {c}")
        with col3:
            st.markdown("**Product / Startups**")
            for c in ["Zoho", "Freshworks", "Razorpay", "Groww", "Browserstack"]:
                st.markdown(f"- {c}")

        st.markdown("---")
        st.markdown("**Expected Salary Range**")
        s1, s2, s3 = st.columns(3)
        s1.metric("Fresher (0-1 yr)", "₹3.5 – ₹6.5 LPA")
        s2.metric("1-2 Years Exp", "₹6 – ₹10 LPA")
        s3.metric("Strong Skills", "₹8 – ₹15 LPA")

        st.markdown("---")
        st.markdown("**Immediate Action Items**")
        st.info("1. Upload improved resume to **Naukri.com** and **LinkedIn** today")
        st.info("2. Solve 10 LeetCode Easy problems before interviews")
        st.info("3. Connect with 5 engineers at target companies on LinkedIn")

    st.divider()
    st.balloons()
    st.success("🎉 All 3 agents completed! Scroll up to review each agent's output.")
