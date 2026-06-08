from django.urls import path

from .views import (
    SkillListView,
    UserSkillCreateView,
    UserSkillListView
)

urlpatterns = [
    path(
        "",
        SkillListView.as_view()
    ),

    path(
        "add/",
        UserSkillCreateView.as_view()
    ),

    path(
        "my-skills/",
        UserSkillListView.as_view()
    ),
]
from .views import (
    SkillListView,
    UserSkillCreateView,
    UserSkillListView,
    SearchUsersView,
)

urlpatterns = [
    path("", SkillListView.as_view()),

    path("add/", UserSkillCreateView.as_view()),

    path("my-skills/", UserSkillListView.as_view()),

    path(
        "search/",
        SearchUsersView.as_view()
    ),
]