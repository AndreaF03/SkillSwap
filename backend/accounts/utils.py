from django.db.models import Avg

from reviews.models import Review
from exchange.models import ExchangeRequest


def calculate_trust_score(user):

    avg_rating = (
        Review.objects.filter(
            reviewed_user=user
        )
        .aggregate(
            Avg("rating")
        )["rating__avg"]
        or 0
    )

    completed_sessions = (
        ExchangeRequest.objects.filter(
            status="COMPLETED"
        )
        .filter(
            receiver=user
        )
        .count()
    )

    rating_score = avg_rating * 20

    completed_score = min(
        completed_sessions * 10,
        100
    )

    activity_score = min(
        user.activity_score,
        100
    )

    trust_score = (
        rating_score * 0.6
        + completed_score * 0.3
        + activity_score * 0.1
    )

    return round(
        trust_score,
        2
    )
