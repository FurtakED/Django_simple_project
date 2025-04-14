from django import forms
from .models import Word, Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name']

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['english_word', 'translation', 'image', 'lesson']
