from google import genai
import os


def get_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not configured")

    return genai.Client(api_key=api_key)


def generate_response(prompt):
    try:
        client = get_client()

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"AI Error: {str(e)}"


def get_related_skills(skill_name):

    prompt = f"""
    Skill:
    {skill_name}

    List 10 related skills.

    Return comma separated values only.
    """

    return generate_response(prompt)


def get_required_skills(goal):

    prompt = f"""
    Career Goal:
    {goal}

    Return only a comma separated list of skills required.

    Example:
    Python, Machine Learning, Deep Learning
    """

    return generate_response(prompt)