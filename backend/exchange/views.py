from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import ExchangeRequest
from .serializers import ExchangeRequestSerializer
class SendRequestView(generics.CreateAPIView):

    serializer_class = ExchangeRequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            sender=self.request.user
        )
class SentRequestsView(generics.ListAPIView):

    serializer_class = ExchangeRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return ExchangeRequest.objects.filter(
            sender=self.request.user
        )
from rest_framework.views import APIView
from rest_framework.response import Response


class AcceptRequestView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        exchange = ExchangeRequest.objects.get(
            id=pk
        )

        exchange.status = "ACCEPTED"
        exchange.save()

        return Response({
            "message": "Request accepted"
        })
class CompleteRequestView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        exchange = ExchangeRequest.objects.get(
            id=pk
        )

        exchange.status = "COMPLETED"
        exchange.save()

        return Response({
            "message": "Exchange completed"
        })
class MyRequestsView(generics.ListAPIView):

    serializer_class = ExchangeRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return ExchangeRequest.objects.filter(
            receiver=self.request.user
        )