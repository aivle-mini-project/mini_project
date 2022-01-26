
from django.db import models
from EDuser.models import Eduser
from .validation import validate_sentence

# Create your models here.


class Diary(models.Model):
  writer = models.ForeignKey(Eduser, on_delete=models.CASCADE, null=True) 
  write = models.TextField(max_length = 100, 
                          verbose_name='일기', 
                          validators=[validate_sentence])
  emotion = models.CharField(max_length =30,verbose_name='감정')
  neutral = models.FloatField(verbose_name='평온')
  positive = models.FloatField(verbose_name='긍정')
  negative = models.FloatField(verbose_name='부정')
  register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

  class Meta:
    db_table = 'diary'
    verbose_name = '일기'
    verbose_name_plural = '일기'
    ordering = ['-id']

  def __str__(self):
    return str(self.writer)

    

class DiaryDetail(models.Model):
  diary = models.ForeignKey(Diary, on_delete= models.CASCADE, verbose_name='writer')
  write = models.TextField(verbose_name='일기')
  emotion = models.CharField(max_length =30,verbose_name='감정')
  neutral = models.FloatField(verbose_name='평온')
  positive = models.FloatField(verbose_name='긍정')
  negative = models.FloatField(verbose_name='부정')

  class Meta:
    db_table = 'diary_detail'
    verbose_name = '일기상세'
    verbose_name_plural = '일기상세'

  def __str__(self):
    return str(self.diary.writer)



class DiaryDetailHighlight(models.Model):
  diary_detail = models.ForeignKey(DiaryDetail, on_delete= models.CASCADE, verbose_name='writer')
  offset = models.IntegerField(verbose_name='시작점')
  length = models.IntegerField(verbose_name='길이')

  class Meta:
    db_table = 'diary_detail_highlight'
    verbose_name = '일기상세효과'
    verbose_name_plural = '일기상세효과'
  
  def __str__(self):
    return str(self.diary_detail.diary.writer)


class Expression(models.Model):
  user = models.ForeignKey(Eduser, on_delete=models.CASCADE)
  diary = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='expressions')
  class Meta:
    db_table='expression'
    verbose_name = '좋아요'
    verbose_name_plural = '좋아요'
    