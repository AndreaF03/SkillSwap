from django.urls import path
from .views import (
    SkillDescriptionView,
    SkillGapAnalyzerView,
    MentorRecommendationView,
    SemanticMatchView
)

urlpatterns = [
    path(
        "skill-description/",
        SkillDescriptionView.as_view()
    ),

    path(
        "skill-gap/",
        SkillGapAnalyzerView.as_view()
    ),

    path(
        "mentor-recommendations/",
        MentorRecommendationView.as_view()
    ),
    path(
    "semantic-match/",
    SemanticMatchView.as_view()
)
]