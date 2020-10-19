from django.urls import path

from perimeter.perimeter_webapp.perimeter_dashboard.views.nodes import json

urlpatterns = [
    path('', json.hello)
]
