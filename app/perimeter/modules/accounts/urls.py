#!/usr/bin/env python3

from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
            template_name="accounts/module_blocks/users/login.dtl.html",
        )
    ),
    path('register/', views.RegisterView.as_view()),
    path('list/', views.index),
    path('<int:user_id>/show/', views.show),
    path('<int:user_id>/edit/', views.edit),
]