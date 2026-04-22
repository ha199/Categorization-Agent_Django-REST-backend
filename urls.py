from django.urls import path
from api.views import categorize_transaction

urlpatterns = [
    path("api/categorize/", categorize_transaction),
]