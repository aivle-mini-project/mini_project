from django.db import models
from diary.models import Diary
from EDuser.models import Eduser
# Create your models here.

class Expression:
  user = models.ForeignKey(Eduser, on_delete=models.CASCADE)
  diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
  class Meta:
    db_table='expression'
    verbose_name = '좋아요'
    verbose_name_plural = '좋아요'