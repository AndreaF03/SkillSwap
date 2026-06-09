from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Skill, UserSkill
from .serializers import (
    SkillSerializer,
    UserSkillSerializer
)


class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class UserSkillCreateView(generics.CreateAPIView):
    serializer_class = UserSkillSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserSkillListView(generics.ListAPIView):
    serializer_class = UserSkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserSkill.objects.filter(
            user=self.request.user
        )
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserSkill


class SearchUsersView(APIView):

    def get(self, request):

        skill_name = request.GET.get("skill")

        if not skill_name:
            return Response(
                {"error": "skill parameter required"},
                status=400
            )

        users = UserSkill.objects.filter(
            skill__name__icontains=skill_name,
            skill_type="TEACH"
        )

        results = []

        for item in users:

            results.append({
                "id": item.user.id,
                "username": item.user.username,
                "location": item.user.location,
                "trust_score": item.user.trust_score,
                "skill": item.skill.name,
            })

        return Response(results)
    
class MatchSuggestionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        current_user = request.user

        teach_skills = UserSkill.objects.filter(
            user=current_user,
            skill_type="TEACH"
        )

        matches = []

        for teach in teach_skills:

            learners = UserSkill.objects.filter(
                skill=teach.skill,
                skill_type="LEARN"
            ).exclude(
                user=current_user
            )

            for learner in learners:

                matches.append({
                    "user_id": learner.user.id,
                    "username": learner.user.username,
                    "location": learner.user.location,
                    "skill_needed": teach.skill.name,
                })

        return Response(matches)