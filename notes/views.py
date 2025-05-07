from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Note

# Create your views here.

class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'

class NoteCreateView(CreateView):
    model = Note
    template_name = 'notes/note_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('note-list')

class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'notes/note_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('note-list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note-list')
