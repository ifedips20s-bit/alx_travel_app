from django.urls import path
from . import views

urlpatterns = [
    # Example endpoint
    path('destinations/', views.DestinationList.as_view(), name='destination-list'),
]