from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .services import generate_response


class SkillDescriptionView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        skill = request.data.get("skill")

        answer = generate_response(
            f"Explain {skill} for a beginner in 100 words."
        )

        return Response({
            "description": answer
        })
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .services import generate_response


class SkillGapAnalyzerView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        resume = request.data.get("resume")
        career_goal = request.data.get("career_goal")

        prompt = f"""
        Analyze the following resume.

        Resume:
        {resume}

        Career Goal:
        {career_goal}

        Return:
        1. Current Skills
        2. Missing Skills
        3. Learning Roadmap

        Format the response clearly.
        """

        result = generate_response(prompt)

        return Response({
            "analysis": result
        })
# ai_features/services.py

def get_required_skills(goal):

    prompt = f"""
    Career Goal:
    {goal}

    Return only a list of skills.
    """

    return generate_response(prompt)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from community.models import Pod
from skills.models import UserSkill

from .services import get_required_skills, get_related_skills


class MentorRecommendationView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        goal = request.data.get("goal")

        skills_text = get_required_skills(goal)

        mentors = User.objects.order_by(
            "-trust_score"
        )[:5]

        pods = Pod.objects.all()[:5]

        return Response({
            "goal": goal,
            "recommended_skills": skills_text,
            "recommended_mentors": [
                mentor.username
                for mentor in mentors
            ],
            "recommended_pods": [
                pod.name
                for pod in pods
            ]
        })  
class SemanticMatchView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        skill = request.data.get("skill")

        related = get_related_skills(skill)

        return Response({
            "skill": skill,
            "related_skills": related
        })