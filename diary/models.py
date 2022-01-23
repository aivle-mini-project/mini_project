from django.db import models
from EDuser.models import Eduser
# Create your models here.

class Diary(models.Model):
  writer = models.ForeignKey(Eduser, on_delete=models.SET_NULL, null=True) 
  write = models.TextField(verbose_name='일기')
  emotion = models.IntegerField(verbose_name='감정')
  register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

  def __str__(self):
    return str(self.writer)

  class Meta:
    db_table = 'diary'
    verbose_name = '일기'
    verbose_name_plural = '일기'


