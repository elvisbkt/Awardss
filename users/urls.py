from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.registration, name = "signup"),
    path("profile/<username>/<int:id>/", views.profile, name = "profile"),
    path("profile/<username>/<int:id>/update", views.update_profile, name = "update_profile"),
]