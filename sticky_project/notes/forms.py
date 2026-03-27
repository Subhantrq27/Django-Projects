from django import forms
from .models import Note

# Form to create/edit notes
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'color']