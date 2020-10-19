from django.urls import path

from perimeter.perimeter_webapp.perimeter_dashboard.views.reports import html

urlpatterns = [
    path('', html.index)
]
