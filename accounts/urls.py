from . import views
from django.urls import path


app_name = "accounts"


urlpatterns = [path("note_list/", views.note_list, name="note_list"), path("note_delete/<str:pk>/", views.note_delete, name="note_delete")]
