from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=30) # 제목
    content = models.CharField(max_length=100) # 내용
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
# Create your models here.
