from google import genai
from django.conf import settings

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)
def get_related_skills(skill_name):

    prompt = f"""
    Skill:
    {skill_name}

    List 10 related skills.

    Return comma separated values only.
    """

    return generate_response(prompt)

def generate_response(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"AI Error: {str(e)}"


def get_required_skills(goal):

    prompt = f"""
    Career Goal:
    {goal}

    Return only a comma separated list of skills required.

    Example:
    Python, Machine Learning, Deep Learning
    """

    return generate_response(prompt)
