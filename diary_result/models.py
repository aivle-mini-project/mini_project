from django.db import models
from diary.models import Diary
    

class Tag(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    tag = models.CharField(max_length=140)