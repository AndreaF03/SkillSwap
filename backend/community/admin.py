from django.contrib import admin
from .models import (
    Pod,
    PodMember,
    Challenge,
    ChallengeSubmission
)

admin.site.register(Pod)
admin.site.register(PodMember)
admin.site.register(Challenge)
admin.site.register(ChallengeSubmission)