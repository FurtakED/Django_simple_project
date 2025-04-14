from django.urls import path
from .views import HomeView, LessonListView, WordListView, LessonCreateView, WordCreateView, FlashcardView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('lessons/', LessonListView.as_view(), name='lesson_list'),
    path('words/', WordListView.as_view(), name='word_list'),
    path('add_lesson/', LessonCreateView.as_view(), name='add_lesson'),
    path('add_word/', WordCreateView.as_view(), name='add_word'),
    path('flashcards/', FlashcardView.as_view(), name='flashcards'),
]
