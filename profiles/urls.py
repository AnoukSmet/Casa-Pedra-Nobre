from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('profle/edit', views.edit_profile, name="edit_profile"),
]
