from django.db import models

class Lesson(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Word(models.Model):
    english_word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='words')

    def __str__(self):
        return self.english_word
