from django.shortcuts import render
from .models import Note
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class NotesListView(ListView):
    model = Note
    template_name = "tasks.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NotesListView, self).dispatch(*args, **kwargs)

class NoteCreateView(CreateView):    
    model = Note
    template_name = 'create_note_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('notelist')

class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'update_note_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('notelist')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'delete_note_form.html'
    success_url = reverse_lazy('notelist')
    success_url = reverse_lazy('notelist')