from crewai import Agent
from langchain_openai import ChatOpenAI


def get_llm():
    return ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)


def create_resume_screening_agent():
    return Agent(
        role="Resume Screening Specialist",
        goal="Analyze a candidate's resume and provide a detailed evaluation of their strengths, weaknesses, and overall profile.",
        backstory=(
            "You are an expert HR recruiter with 10+ years of experience screening resumes "
            "across software engineering, data science, and product roles. You have a sharp eye "
            "for identifying skill gaps, formatting issues, and areas where candidates undersell themselves. "
            "You provide structured, honest, and actionable feedback."
        ),
        llm=get_llm(),
        verbose=True,
        allow_delegation=False,
    )


def create_resume_improvement_agent():
    return Agent(
        role="Resume Enhancement Coach",
        goal="Rewrite and enhance the candidate's resume to make it ATS-friendly, impactful, and competitive in the job market.",
        backstory=(
            "You are a professional resume writer and career coach who has helped thousands of candidates "
            "land jobs at top companies including FAANG, startups, and MNCs. You know exactly how to "
            "quantify achievements, use strong action verbs, tailor content for specific roles, and "
            "structure a resume to pass ATS filters. You transform average resumes into standout documents."
        ),
        llm=get_llm(),
        verbose=True,
        allow_delegation=False,
    )


def create_job_search_agent():
    return Agent(
        role="Job Search Strategist",
        goal="Find and recommend the most relevant job opportunities that match the candidate's improved profile.",
        backstory=(
            "You are a seasoned talent acquisition specialist and career consultant who tracks the job market daily. "
            "You know which companies are actively hiring, what roles suit different experience levels, "
            "and how to match candidate profiles with job requirements. You provide curated job recommendations "
            "along with application tips and preparation advice tailored to each opportunity."
        ),
        llm=get_llm(),
        verbose=True,
        allow_delegation=False,
    )
