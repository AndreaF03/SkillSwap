from rest_framework import serializers
from .models import ExchangeRequest


class ExchangeRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExchangeRequest
        fields = "__all__"
        read_only_fields = [
            "sender",
            "status",
            "created_at"
        ]