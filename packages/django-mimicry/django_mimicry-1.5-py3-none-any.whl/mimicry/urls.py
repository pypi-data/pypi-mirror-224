"""
URL Configuration for the simulate_user app.

This module contains the URL patterns for the app's views.

Routes:
- `/switch_user/`: The endpoint to handle the switching or simulating of different users.

Functions:
- `switch_user`: View function to handle user switching logic.

Usage:
Make sure to include these URL patterns in the project's main `urls.py` file using Django's `include()` function.
"""

from django.urls import path
from .views import switch_user

urlpatterns: list = [
    path('switch_user/', switch_user, name='mimicry_switch_user'),
]
