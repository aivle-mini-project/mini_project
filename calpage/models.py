from django.db import models
from django.db.models.fields import IntegerField

class Calemotion(models.Model):
    id = IntegerField(primary_key=True)
    emo_date = models.DateField(null=False)
    emotion = models.CharField(max_length=30,null=False)
    emoji = models.CharField(max_length=30)

    class Meta:
        db_table = 'calemotion'
        managed = False
