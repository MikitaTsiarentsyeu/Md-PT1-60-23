from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesListView.as_view(), name="notemain"),
    path('note/list', views.NotesListView.as_view(), name="notelist"),
    path('note/notecreate', views.NoteCreateView.as_view(),  name="createnote"),
    path('note/noteupdate/<pk>', views.NoteUpdateView.as_view(), name="updatenote"),
    path('note/notedelete/<pk>', views.NoteDeleteView.as_view(), name="deletenote"),
]