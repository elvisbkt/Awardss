from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_index, name="landing_index"),
    path("post/new", views.WebPostView.as_view(), name = "post_web"),
    path('search/', views.search_results, name='search_results'),
    path("website/<int:pk>/", views.WebsiteDetailView.as_view(), name = "website_detail"),
    path('like/', views.website_like, name='like'),


]