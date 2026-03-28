from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search-result"),
    path("wiki/<str:title>", views.title, name="show-entry"),
    path("new", views.new, name="new"),
    path("created", views.created, name="created"),
    path("edit/<str:title>", views.edit, name="edit")
]
