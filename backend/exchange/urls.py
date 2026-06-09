from django.urls import path

from .views import (
    SendRequestView,
    MyRequestsView,
    SentRequestsView,
    AcceptRequestView,
    CompleteRequestView,
)

urlpatterns = [

    path(
        "send/",
        SendRequestView.as_view()
    ),

    path(
        "received/",
        MyRequestsView.as_view()
    ),

    path(
        "sent/",
        SentRequestsView.as_view()
    ),

    path(
        "<int:pk>/accept/",
        AcceptRequestView.as_view()
    ),

    path(
        "<int:pk>/complete/",
        CompleteRequestView.as_view()
    ),
]