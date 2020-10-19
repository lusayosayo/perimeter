from django.urls import path

from . import views

urlpatterns = [
    path('service/<int:service_mapping_id>/invoke', views.check_service)
]