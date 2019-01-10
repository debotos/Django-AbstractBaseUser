from django.urls import path

from .views import login, credit_request, screenshot

urlpatterns = [
    path('login/', login),
    path('credit/', credit_request),  # Asking for Credit
    path('screenshot/', screenshot)  # Making a screenshot so reduce Credit point
]
