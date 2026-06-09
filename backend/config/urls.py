from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls")),
    path(
    "api/skills/",
    include("skills.urls")
),
path(
    "api/exchange/",
    include("exchange.urls")
),
path(
    "api/ai/",
    include("ai_features.urls")
),
]