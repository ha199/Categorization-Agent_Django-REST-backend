from django.urls import path
from views import categorize_transaction

urlpatterns = [
    path('api/categorize/', categorize_transaction, name='categorize'),
]
