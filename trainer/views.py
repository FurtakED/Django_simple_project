from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .models import Lesson, Word
from .forms import LessonForm, WordForm

class HomeView(TemplateView):
    template_name = 'home.html'

class LessonListView(ListView):
    model = Lesson
    template_name = 'lesson_list.html'
    context_object_name = 'lessons'

class WordListView(ListView):
    model = Word
    template_name = 'word_list.html'
    context_object_name = 'words'

# class LessonCreateView(CreateView):
#     model = Lesson
#     form_class = LessonForm
#     template_name = 'lesson_form.html'
#     success_url = reverse_lazy('lesson_list')
class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'lesson_form.html'
    success_url = reverse_lazy('lesson_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("Form:", context['form'])  # Debug output
        return context

class WordCreateView(CreateView):
    model = Word
    form_class = WordForm
    template_name = 'word_form.html'
    success_url = reverse_lazy('word_list')

class FlashcardView(ListView):
    model = Word
    template_name = 'flashcards.html'
    context_object_name = 'words'
