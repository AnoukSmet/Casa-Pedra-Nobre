from django.urls import path
from . import views

urlpatterns = [
    path('', views.tourist_info, name="tourist_info"),
    path('<int:recommendation_id>', views.recommendation_detail,
         name="recommendation_detail"),
    path('add/', views.add_recommendation, name='add_recommendation'),
    path('<int:recommendation_id>/edit', views.edit_recommendation,
         name="edit_recommendation"),
    path('add-to-favorites/<recommendation_id>/', views.add_to_favorites,
         name='add_to_favorites'),
]
