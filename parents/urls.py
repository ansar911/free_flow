from django.urls import path
from . import views

urlpatterns = [
    path("", views.parent_list, name="parent_list"),
    path("add/", views.add_parent, name="add_parent"),
    path("edit/<int:pk>/", views.edit_parent, name="edit_parent"),
]