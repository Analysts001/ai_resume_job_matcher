def build_prompt(resume, job):

    return f"""
You are an expert HR recruiter.

Compare Resume and Job Description.

Return:

1. Match Score (0-100)
2. Matching Skills
3. Missing Skills
4. Improvement Suggestions
5. Final Verdict

RESUME:
{resume}

JOB DESCRIPTION:
{job}
"""