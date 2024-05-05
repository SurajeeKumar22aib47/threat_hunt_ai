

from django.urls import path
from threathunt_ai.views import predictions_view

urlpatterns = [
    path('', predictions_view, name='display_results'),
]
