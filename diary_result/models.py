from django.db import models
from taggit.managers import TaggableManager
from diary.models import Diary

class tagmodel(models.Model):
    tags = TaggableManager(blank=True)
    

class Tag(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    tag = models.CharField(max_length=140)