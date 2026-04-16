from crewai import Crew, Process
from agents import (
    create_resume_screening_agent,
    create_resume_improvement_agent,
    create_job_search_agent,
)
from tasks import (
    create_screening_task,
    create_improvement_task,
    create_job_search_task,
)


def run_job_search_crew(resume_text: str) -> dict:
    """
    Runs the multi-agent job search pipeline on the provided resume text.
    Returns a dict with outputs from all three agents.
    """
    # Create agents
    screening_agent = create_resume_screening_agent()
    improvement_agent = create_resume_improvement_agent()
    job_search_agent = create_job_search_agent()

    # Create tasks (chained: each builds on the previous)
    screening_task = create_screening_task(screening_agent, resume_text)
    improvement_task = create_improvement_task(improvement_agent, resume_text, screening_task)
    job_search_task = create_job_search_task(job_search_agent, improvement_task)

    # Assemble the crew
    crew = Crew(
        agents=[screening_agent, improvement_agent, job_search_agent],
        tasks=[screening_task, improvement_task, job_search_task],
        process=Process.sequential,
        verbose=2,
    )

    result = crew.kickoff()
    return {
        "screening_report": screening_task.output.raw_output if screening_task.output else "",
        "improved_resume": improvement_task.output.raw_output if improvement_task.output else "",
        "job_recommendations": job_search_task.output.raw_output if job_search_task.output else "",
        "final_output": result,
    }
