from django.urls import path
from . import views

urlpatterns = [
    path('', views.tourist_info, name="tourist_info"),
    path('tourist-info/<int:recommendation_id>', views.recommendation_detail, name="recommendation_detail"),
    path('add-to-favorites/<recommendation_id>/', views.add_to_favorites, name='add_to_favorites'),
]
