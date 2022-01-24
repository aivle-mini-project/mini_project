from django.db import models
from django.db.models.fields import DateField, FloatField, IntegerField


class Statistics(models.Model):
    id2 = IntegerField(primary_key=True)
    emo_date = models.DateField(null=False)
    positive = models.FloatField(default=0, null=True)
    negative = models.FloatField(default=0, null=True)
    neutral = models.FloatField(default=0, null=True)

    class Meta:
        db_table = 'statistics'
        managed = False
