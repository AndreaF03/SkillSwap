from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Review
from .serializers import ReviewSerializer
from accounts.utils import calculate_trust_score
class CreateReviewView(
    generics.CreateAPIView
):

    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(
        self,
        serializer
    ):

        review = serializer.save(
            reviewer=self.request.user
        )

        reviewed_user = (
            review.reviewed_user
        )

        reviewed_user.trust_score = (
            calculate_trust_score(
                reviewed_user
            )
        )

        reviewed_user.save()