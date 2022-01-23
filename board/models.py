from tabnanny import verbose
from django.db import models

# Create your models here.
class Stastics(models.Model):
  register_date = models.DateField()
  good = models.IntegerField()
  bad = models.IntegerField()
  emotion1 = models.IntegerField()
  emotion2 = models.IntegerField()
  emotion3 = models.IntegerField()

  class Meta:
    db_table='stastics'
    verbose_name = '통계'
    verbose_name_plural = '통계'


