from crewai import Task


def create_screening_task(agent, resume_text: str) -> Task:
    return Task(
        description=f"""
Analyze the following resume thoroughly:

---RESUME START---
{resume_text}
---RESUME END---

Your analysis must cover:
1. **Overall Impression** - First impression score (1-10) and reasoning
2. **Technical Skills Evaluation** - Are the listed skills relevant and well-presented?
3. **Experience & Projects** - Quality, impact, and quantification of experience
4. **Education** - How education is presented
5. **Formatting & ATS Compatibility** - Structure, keywords, readability
6. **Key Strengths** - Top 3 strengths
7. **Critical Weaknesses** - Top 3 areas needing improvement
8. **Missing Elements** - What important sections/information is absent?

Provide a structured report that the improvement agent can act on.
""",
        expected_output=(
            "A detailed resume analysis report with sections covering overall impression, "
            "skills evaluation, experience quality, ATS compatibility, strengths, weaknesses, "
            "and missing elements with specific improvement suggestions."
        ),
        agent=agent,
    )


def create_improvement_task(agent, resume_text: str, screening_task: Task) -> Task:
    return Task(
        description=f"""
Using the resume screening analysis provided, rewrite and enhance the following resume:

---ORIGINAL RESUME---
{resume_text}
---END RESUME---

Your enhanced resume must:
1. **Fix all identified weaknesses** from the screening report
2. **Quantify achievements** wherever possible (add metrics, percentages, numbers)
3. **Use strong action verbs** at the start of each bullet point
4. **Add missing sections** (Summary, Skills matrix, etc.)
5. **Optimize for ATS** with relevant keywords for software/tech roles
6. **Improve formatting** for clarity and impact
7. **Tailor the summary** to highlight the candidate's best attributes

Output the complete rewritten resume in a clean, professional format.
Also list the **Top 5 Key Changes Made** as a summary at the end.
""",
        expected_output=(
            "A completely rewritten, ATS-optimized professional resume with quantified achievements, "
            "strong action verbs, proper formatting, and a summary of the top 5 key changes made."
        ),
        agent=agent,
        context=[screening_task],
    )


def create_job_search_task(agent, improvement_task: Task) -> Task:
    return Task(
        description="""
Based on the improved resume profile, identify and recommend suitable job opportunities.

Your job search recommendations must include:
1. **Recommended Job Roles** - List 5-7 job titles that match the candidate's profile
2. **Target Companies** - List 10+ companies (mix of startups, MNCs, product companies) actively hiring
3. **Top Job Boards & Platforms** - Where to search (LinkedIn, Naukri, Indeed, etc.) with search tips
4. **Salary Range** - Expected compensation range for each role level
5. **Skills to Prioritize** - Which skills to highlight for each role type
6. **Application Tips** - 5 specific tips to maximize interview chances
7. **Immediate Action Items** - 3 things the candidate should do this week

Make recommendations realistic and achievable based on the candidate's current profile.
""",
        expected_output=(
            "A comprehensive job search strategy with recommended roles, target companies, "
            "job platforms, salary ranges, application tips, and immediate action items "
            "tailored to the candidate's improved profile."
        ),
        agent=agent,
        context=[improvement_task],
    )
