from django.db import models

# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    total_marks = models.IntegerField()
    score = models.IntegerField()

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True,)
    question = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    diagram = models.ImageField(default='default.png', blank=True)
    marks = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)

    def __str__(self):
        return self.question
